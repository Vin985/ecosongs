import librosa
import numpy as np

from spectrograms import create_image, create_spectrogram, generate_composite

offset = 0
duration = 15
file_path = "../../data/wav/test_real.wav"

audio, sr = librosa.load(file_path, sr=None)

start = offset * sr
end = start + duration * sr
sample = audio[start:end]

# im = create_spectrogram(
#     sample,
#     duration=duration,
#     n_fft=512,
#     contrast=1.5,
#     remove_noise=False,
#     color_mask=(255, 0, 0))
# im = create_spectrogram(
#     sample,
#     duration=duration,
#     n_fft=2048,
#     contrast=1.5,
#     remove_noise=True,
#     color_mask=(255, 0, 0))

# im = create_spectrogram(
#     audio,
#     duration=duration,
#     n_fft=2048,
#     contrast=1.5,
#     remove_noise=True,
#     color_mask=(255, 0, 0))
# im.show()

# res = generate_composite(
#     sample,
#     n_fft=[128, 512, 2048],
#     color_masks=[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
#     duration=duration)
# res.show()
# res.save("test.png")

#
# create_spectrogram(y, sr, offset=295, duration=25, n_fft=128, contrast=1.5)
# create_spectrogram(y, sr, offset=295, duration=25, n_fft=512, contrast=1.5)
# create_spectrogram(y, sr, offset=295, duration=25, n_fft=2048, contrast=1.5)
#
# create_spectrogram(
#     y,
#     sr,
#     offset=295,
#     duration=25,
#     n_fft=512,
#     contrast=1.5,
#     remove_noise=False)
# im1 = create_spectrogram(
#     y,
#     sr,
#     offset=300,
#     duration=15,
#     n_fft=512,
#     contrast=1.5,
#     color_mask=(255, 0, 0))
# im2 = create_spectrogram(
#     y,
#     sr,
#     offset=300,
#     duration=15,
#     n_fft=128,
#     contrast=1.5,
#     color_mask=(0, 255, 0))
# im3 = create_spectrogram(
#     y,
#     sr,
#     offset=300,
#     duration=15,
#     n_fft=2048,
#     contrast=2,
#     color_mask=(0, 0, 255))
# im1.show()
# im2.show()
# im3.show()
# ia1 = np.asarray(im1)
# ia2 = np.asarray(im2)
# ia3 = np.asarray(im3)
# iaf = ia1 + ia2 + ia3
# imf = Image.fromarray(iaf, mode='RGB')
# imf.show()
# print(iaf)
# S = librosa.stft(y2, n_fft=1024)
# D = librosa.amplitude_to_db(S, ref=np.max, top_db=60.0)
# mg, phase = librosa.magphase(S)
#
# create_image(D, show=True, contrast=2)
#
# s2 = remove_noiseInSpectro(
#     mg, histo_relative_size=8, window_smoothing=5, N=0.1, dB=True, plot=False)
# create_image(s2.astype("float32"), show=True, contrast=1.5)
