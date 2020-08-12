import os
import pickle
import traceback
from pathlib import Path

import librosa
import numpy as np
import tensorflow as tf
import tf_slim as slim
import yaml
from scipy.ndimage.interpolation import zoom
from tqdm import tqdm

from lib.data_helpers import load_annotations
from lib.train_helpers import SpecSampler, create_net


class CityNetTrainer:
    def __init__(self, opts):
        self.opts = opts
        self.paths = self.set_paths()

    def set_paths(self):
        paths = {}
        base = self.opts["base_dir"]
        paths["train_root_dir"] = base + self.opts["train_dir"]
        paths["test_root_dir"] = base + self.opts["test_dir"]
        paths["train_spec_dir"] = (
            paths["train_root_dir"]
            + self.opts["dest_dir"]
            + self.opts["spec_type"]
            + "/"
        )
        paths["test_spec_dir"] = (
            paths["test_root_dir"]
            + self.opts["dest_dir"]
            + self.opts["spec_type"]
            + "/"
        )
        return paths

    def create_detection_dataset(self, data_type="train"):
        base = self.paths[data_type + "_root_dir"]
        dest_dir = base + self.opts["dest_dir"]
        audio_dir = base + self.opts["audio_dir"]
        labels_dir = base + self.opts["annotations_dir"]

        # load in the annotations
        save_dir = Path(dest_dir + self.opts.get("spec_type", "mel") + "/")
        if not save_dir.exists():
            save_dir.mkdir(parents=True)

        for fname in os.listdir(audio_dir):
            savename = save_dir / fname.replace(".wav", ".pkl")

            # load the annottion
            try:
                if not os.path.exists(savename):
                    annots, wav, sample_rate = load_annotations(
                        fname, audio_dir, labels_dir
                    )

                    spec = self.generate_spectrogram(wav, sample_rate)

                    # save to disk
                    with open(savename, "wb") as f:
                        pickle.dump((annots, spec), f, -1)
                else:
                    print("Skipping " + str(savename))
            except Exception:
                print("Error loading: " + fname + ", skipping.")
                print(traceback.format_exc())

    def generate_spectrogram(self, wav, sample_rate):

        if self.opts["spec_type"] == "mel":
            spec = librosa.feature.melspectrogram(
                wav,
                sr=sample_rate,
                n_fft=self.opts.get("n_fft", 2048),
                hop_length=self.opts.get("hop_length", 1024),
                n_mels=self.opts.get("n_mels", 32),
            )
            spec = spec.astype(np.float32)
        else:
            raise AttributeError("No other spectrogram supported yet")
        return spec

    def load_data_helper(self, file_name):

        annots, spec = pickle.load(open(file_name, "rb"))
        annots = annots[self.opts["classname"]]
        # reshape annotations
        factor = float(spec.shape[1]) / annots.shape[0]
        annots = zoom(annots, factor)
        # create sampler
        if not self.opts["learn_log"]:
            spec = np.log(self.opts["A"] + self.opts["B"] * spec)
            spec = spec - np.median(spec, axis=1, keepdims=True)

        return annots, spec

    def load_data(self, data_type="train"):
        # load data and make list of specsamplers
        X = []
        y = []

        src_dir = self.paths[data_type + "_spec_dir"]
        for file_name in os.listdir(src_dir)[0:100]:
            print("Loading file: ", file_name)
            annots, spec = self.load_data_helper(src_dir + file_name)
            X.append(spec)
            y.append(annots)

        height = min(xx.shape[0] for xx in X)
        X = [xx[-height:, :] for xx in X]

        return X, y

    @staticmethod
    def force_make_dir(dirpath):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        return dirpath

    def train_and_test(
        self,
        train_X,
        test_X,
        train_y,
        test_y,
        test_files,
        TEST_FOLD=99,
        val_X=None,
        val_y=None,
    ):
        """
        Doesn't do any data loading - assumes the train and test data are passed
        in as parameters!
        """
        if val_X is None:
            val_X = test_X
            val_y = test_y

        print("in train and test")
        tf.compat.v1.disable_eager_execution()

        # # creaging samplers and batch iterators
        train_sampler = SpecSampler(
            64,
            self.opts["HWW_X"],
            self.opts["HWW_Y"],
            self.opts["do_augmentation"],
            self.opts["learn_log"],
            randomise=True,
            balanced=True,
        )
        test_sampler = SpecSampler(
            64,
            self.opts["HWW_X"],
            self.opts["HWW_Y"],
            False,
            self.opts["learn_log"],
            randomise=False,
            seed=10,
            balanced=True,
        )

        height = train_X[0].shape[0]
        net = create_net(
            height,
            self.opts["HWW_X"],
            self.opts["HWW_Y"],
            self.opts["num_filters"],
            self.opts["wiggle_room"],
            self.opts["conv_filter_width"],
            self.opts["num_dense_filters"],
            self.opts["do_batch_norm"],
        )

        y_in = tf.compat.v1.placeholder(tf.int32, (None))
        x_in = net["input"]

        print("todo - fix this up...")
        trn_output = net["fc8"]
        test_output = net["fc8"]

        _trn_loss = tf.reduce_mean(
            tf.nn.sparse_softmax_cross_entropy_with_logits(
                logits=trn_output, labels=y_in
            )
        )
        _test_loss = tf.compat.v1.reduce_mean(
            tf.nn.sparse_softmax_cross_entropy_with_logits(
                logits=test_output, labels=y_in
            )
        )
        print(y_in, trn_output, tf.argmax(trn_output, axis=1))

        pred = tf.cast(tf.argmax(trn_output, axis=1), tf.int32)
        _trn_acc = tf.reduce_mean(tf.cast(tf.equal(y_in, pred), tf.float32))

        pred = tf.cast(tf.argmax(test_output, axis=1), tf.int32)
        _test_acc = tf.reduce_mean(tf.cast(tf.equal(y_in, pred), tf.float32))

        optimizer = tf.compat.v1.train.AdamOptimizer(
            learning_rate=self.opts["learning_rate"], beta1=0.5, beta2=0.9
        )

        train_op = slim.learning.create_train_op(_trn_loss, optimizer)

        saver = tf.compat.v1.train.Saver(max_to_keep=5)

        with tf.compat.v1.Session() as sess:

            sess.run(tf.compat.v1.global_variables_initializer())

            for epoch in range(self.opts["max_epochs"]):

                print("training epoch #", epoch)

                ######################
                # TRAINING
                trn_losses = []
                trn_accs = []

                for xx, yy in tqdm(train_sampler(train_X, train_y)):
                    trn_ls, trn_acc, _ = sess.run(
                        [_trn_loss, _trn_acc, train_op], feed_dict={x_in: xx, y_in: yy}
                    )
                    trn_losses.append(trn_ls)
                    trn_accs.append(trn_acc)

                ######################
                # VALIDATION
                val_losses = []
                val_accs = []

                for xx, yy in test_sampler(test_X, test_y):
                    val_ls, val_acc = sess.run(
                        [_test_loss, _test_acc], feed_dict={x_in: xx, y_in: yy}
                    )
                    val_losses.append(val_ls)
                    val_accs.append(val_acc)

                print(
                    " %03d :: %02f  -  %02f  -  %02f  -  %02f"
                    % (
                        epoch,
                        np.mean(trn_losses),
                        np.mean(trn_accs),
                        np.mean(val_losses),
                        np.mean(val_accs),
                    )
                )

            #######################
            # TESTING
            results_savedir = self.force_make_dir(
                self.paths["logging_dir"] + "results/"
            )
            predictions_savedir = self.force_make_dir(
                self.paths["logging_dir"] + "per_file_predictions/"
            )

            test_sampler = SpecSampler(
                64,
                self.opts["HWW_X"],
                self.opts["HWW_Y"],
                False,
                self.opts["learn_log"],
                randomise=False,
                seed=10,
                balanced=False,
            )
            for fname, spec, y in zip(test_files, test_X, test_y):
                probas = []
                y_true = []
                for Xb, yb in test_sampler([spec], [y]):
                    preds = sess.run(test_output, feed_dict={x_in: Xb})
                    probas.append(preds)
                    y_true.append(yb)

                y_pred_prob = np.vstack(probas)
                y_true = np.hstack(y_true)
                y_pred = np.argmax(y_pred_prob, axis=1)

                print("Saving to {}".format(predictions_savedir))
                with open(predictions_savedir + fname, "wb") as f:
                    pickle.dump([y_true, y_pred_prob], f, -1)

            # save weights from network
            saver.save(sess, results_savedir + "weights_%d.pkl" % 1, global_step=1)

    def train(self):

        # X: spectrograms, y: labels
        train_X, train_y = self.load_data("train")
        test_X, test_y = self.load_data("test")

        print("data_loaded")

        test_files = os.listdir(self.paths["test_spec_dir"])

        for idx in range(self.opts["ensemble_members"]):
            print("train ensemble: ", idx)
            self.paths["logging_dir"] = self.opts[
                "base_dir"
            ] + "predictions/%s/%d/%s/" % (
                self.opts["run_type"],
                idx,
                self.opts["classname"],
            )
            self.force_make_dir(self.paths["logging_dir"])
            # sys.stdout = ui.Logger(logging_dir + "log.txt")

            with open(self.paths["logging_dir"] + "network_opts.yaml", "w") as f:
                yaml.dump(self.opts, f, default_flow_style=False)

            self.train_and_test(
                train_X, test_X, train_y, test_y, test_files,
            )

