import librosa

import config
from analyse.image import ImageGenerator
from analyse.spectrogram import SpectrogramGenerator
from audio.recording import Recording

conf = config.Config("ecosongs.conf")
specgen = SpectrogramGenerator(conf.spectrogram)
imgen = ImageGenerator(conf.image)

r = Recording("../../data/wav/test_real.wav", specgen, "")
sample = r.getSample(0, 15)

im = imgen.spec2img(sample.get_spectrogram().spec)
im.show()
# print(r.get_ACI(time_step=15))
#

# print(sample.get_ACI())
#
# im = imgen.generate_composite(sample, specgen)
# im.show()
