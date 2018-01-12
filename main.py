import timeit

import config
from audiofile import Recording
from image import ImageGenerator
from spectrogram import SpectrogramGenerator

conf = config.Config("ecosongs.conf")
specgen = SpectrogramGenerator(conf.spectrogram)
imgen = ImageGenerator(conf.image)

r = Recording("../../data/wav/test_real.wav")
sample = r.getSample(0, 15)

sample.generate_spectrograms(specgen)

imgen.generate_composite(sample.spectrograms)

t2 = timeit.Timer(
    "imgen.generate_composite(sample.spectrograms)", globals=globals())
print(t2.repeat(number=50))

#imgen.create_image(sample, 512, show=True)

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
