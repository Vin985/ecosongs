import yaml
import os

try:
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
except:
    pass

from training.utils import create_detection_dataset

if __name__ == "__main__":

    stream = open("CONFIG.yaml", "r")
    opts = yaml.load(stream, Loader=yaml.Loader)
    print(opts)

    create_detection_dataset(opts)
    create_detection_dataset(opts, train=False)
    # spec_dir = generate_spectrograms(extracted_dir, extracted_dir + "spectrograms/")

