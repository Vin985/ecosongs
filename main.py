import configparser

from audiofile import Recording
from generators import SpectrogramGenerator

#from spectrograms import create_image

config = configparser.ConfigParser()
config.read("ecosongs.conf")

r = Recording("../../data/wav/test_real.wav")

specgen = SpectrogramGenerator(config)

sample = r.getSample(0, 15)

print(sample)
print(sample.length / sample.sr)

# file_path = "../../data/wav/test_real.wav"
#
# audio, sr = librosa.load(file_path, sr=None)
# start = offset * sr
# end = start + duration * sr
# sample = audio[start:end]

# res = create_image(
#     sample=sample,
#     n_fft=512,
#     duration=duration,
#     color_mask=(255, 0, 0),
#     show=True)
