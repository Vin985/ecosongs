import yaml
import os

try:
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
except:
    pass

from training.utils import create_detection_dataset, train_citynet


from training.CityNet_trainer import CityNetTrainer

if __name__ == "__main__":

    stream = open("CONFIG.yaml", "r")
    opts = yaml.load(stream, Loader=yaml.Loader)
    print(opts)

    trainer = CityNetTrainer(opts)
    # trainer.create_detection_dataset("train")
    # trainer.create_detection_dataset("test")
    trainer.train()
    # create_detection_dataset(opts)
    # create_detection_dataset(opts, train=False)
    # train_citynet(opts)
    # spec_dir = generate_spectrograms(extracted_dir, extracted_dir + "spectrograms/")

