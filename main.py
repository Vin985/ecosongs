import configparser

import cv2
import librosa
import numpy as np

import soundfile as sf
from analyse.image import ImageGenerator
from analyse.spectrogram import SpectrogramGenerator
from audio.recording import Recording
from db import models

config = configparser.ConfigParser()
config.read("ecosongs.conf")

specgen = SpectrogramGenerator(config)
imgen = ImageGenerator(config)

#r = Recording(
#    "../../data/acoustic/test/wav/test_real.wav", specgen, audio_type="")
r = Recording(
    "../../data/acoustic/test/audiomoth/outside park/16k_g5_rect_smallH_street.WAV",
    recorder="")


# for record in models.RecordingModel.select():
#     print("test " + record.name)

# res = librosa.effects.split(r.audio, top_db=10)
# print(res)
# print(r.get_SNR(activity_threshold_dB=5, N=1))
sample = r.get_sample(20, 15)
# print(sample.has_bird(imgen))
# for i in range(0, 600, 15):
#     print(i)
#     sample = r.getSample(i, i + 15)
#     print(sample.has_bird())

## TODO: allow spec2img to accept a Spectrogram object
## NOTE: image might have to be resized to be viewed in fullscreen
spec = sample.get_spectrogram(specgen, n_fft=512)
im = imgen.spec2img(spec.spec, size=(int(299 * spec.duration / 1.5), 299))
im.show()

# orig = np.asarray(im).copy()
# # im.show()
# gray = im.convert('L')
# img = np.asarray(gray).copy()
# #img = cv2.medianBlur(img, 5)
# #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# blurred = cv2.medianBlur(img, 5)
# thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY)[1]
# # cv2.imshow('SPEC', blurred)
# # cv2.waitKey(-1)
# # cv2.imshow('SPEC', thresh)
# # cv2.waitKey(-1)
# x, y, z = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(x)
#
# print(z)
# # draw the contour and center of the shape on the image
# cv2.drawContours(orig, y, -1, (0, 255, 0), 1, cv2.LINE_AA)
#
# # show the image
# cv2.imshow("Image", orig)
# cv2.waitKey(0)

# im.show()
# print(r.get_ACI(time_step=15))
#

# print(sample.get_ACI())
#
# im = imgen.generate_composite(sample, specgen)
# im.show()
