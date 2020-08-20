import tensorflow as tf
from tensorflow.keras import Model, layers, regularizers, Input

from analysis.detection.lib.dl_model import DLModel


class CityNetTF2(DLModel):
    NAME = "CityNetTF2"

    def create_net(self):
        print("init_create_net")
        inputs = Input(
            shape=(
                self.opts["spec_height"],
                self.opts["hww_x"] * 2,
                self.opts["channels"],
            ),
            dtype=tf.float32,
        )
        x = layers.Conv2D(
            self.opts.get("num_filters", 128),
            (
                self.opts["spec_height"] - self.opts["wiggle_room"],
                self.opts["conv_filter_width"],
            ),
            bias_initializer=None,
            padding="valid",
            activation=None,
            name="conv1_1",
            kernel_regularizer=regularizers.l2(0.001),
        )(inputs)
        x = layers.LeakyReLU(alpha=1 / 3)(x)
        x = layers.Conv2D(
            self.opts.get("num_filters", 128),
            (1, 3),
            bias_initializer=None,
            padding="valid",
            activation=None,
            name="conv1_2",
            kernel_regularizer=regularizers.l2(0.001),
        )(x)
        x = layers.LeakyReLU(alpha=1 / 3)(x)
        W = x.shape[2]
        x = layers.MaxPool2D(pool_size=(1, W), strides=(1, 1),)(x)
        x = tf.transpose(x, (0, 3, 2, 1))
        x = layers.Flatten()(x)
        x = layers.Dense(
            self.opts["num_dense_units"],
            activation=None,
            bias_initializer=None,
            kernel_regularizer=regularizers.l2(0.001),
        )(x)
        x = layers.Dropout(self.opts["dropout"])(x)
        x = layers.LeakyReLU(alpha=1 / 3)(x)
        x = layers.Dense(
            self.opts["num_dense_units"],
            activation=None,
            bias_initializer=None,
            kernel_regularizer=regularizers.l2(0.001),
        )(x)
        x = layers.Dropout(self.opts["dropout"])(x)
        x = layers.LeakyReLU(alpha=1 / 3)(x)
        outputs = layers.Dense(
            2, activation=None, kernel_regularizer=regularizers.l2(0.001),
        )(x)
        print("end_layers")
        model = Model(inputs, outputs, name=self.NAME)
        print("after model")
        model.summary()
        return model

    def run_net(self, inputs):
        pass
