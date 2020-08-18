import yaml
import os

# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
# try:
#     os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# except:
#     pass

from training.utils import create_detection_dataset, train_citynet


from training.CityNet_trainer import CityNetTrainer

if __name__ == "__main__":

    stream = open("src/test/citynet2/CONFIG.yaml", "r")
    opts = yaml.load(stream, Loader=yaml.Loader)
    opts["model_name"] = "citynet_dropout2"
    print(opts)

    trainer = CityNetTrainer(opts)
    # trainer.create_detection_dataset("train")
    # trainer.create_detection_dataset("test")
    trainer.train()
    # create_detection_dataset(opts)
    # create_detection_dataset(opts, train=False)
    # train_citynet(opts)
    # spec_dir = generate_spectrograms(extracted_dir, extracted_dir + "spectrograms/")

