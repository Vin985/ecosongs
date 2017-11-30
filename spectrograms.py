import librosa
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

from compute_indice import remove_noiseInSpectro


def prepare_spectrogram(spec, invert=False):
    # Make sure spectrogram is in float32 because pillow doesn't
    # support float64
    spec = spec.astype("float32")
    # Normalize spectrogram in [0:1]
    spec -= spec.min(axis=None)
    spec /= spec.max(axis=None)
    if (invert):
        spec = 1 - spec
    spec = spec * 255
    # flip upside down since writing image start from top left
    spec = np.flipud(spec)
    return spec


def create_image(spec,
                 color_mask,
                 show=False,
                 save=False,
                 contrast=0,
                 invert_colors=False):
    # if spec is in [0:1], make it in [0: 255]

    # spec = librosa.amplitude_to_db(spec, ref=np.max, top_db=80.0)
    spec = prepare_spectrogram(spec, invert=invert_colors)

    # Create image from float points
    img = Image.fromarray(spec, mode='F')
    # Convert in grayscale
    img = img.convert("L")
    # Colorise in red
    img = ImageOps.colorize(img, (0, 0, 0), color_mask)

    # enhance contrast
    if (contrast > 0):
        c_enh = ImageEnhance.Contrast(img)
        img = c_enh.enhance(contrast)

    if (show):
        img.show()
    return img


def create_spectrogram(sample,
                       duration,
                       n_fft,
                       color_mask,
                       remove_noise=True,
                       contrast=1):
    # TODO: add n_fft list to generate multiple spectrograms
    spectro = librosa.stft(sample, n_fft=n_fft)
    mag, phase = librosa.magphase(spectro)

    specdb = librosa.amplitude_to_db(spectro, ref=np.max, top_db=80)

    if (remove_noise):
        specdb = remove_noiseInSpectro(
            specdb,
            histo_relative_size=8,
            window_smoothing=5,
            N=0.1,
            dB=False,
            plot=False)
        specdb = specdb.astype("float32")

    img = create_image(specdb, contrast=contrast, color_mask=color_mask)
    img = img.resize((int(299 * duration / 1.5), 299), Image.BILINEAR)
    return img


def generate_composite(sample, n_fft, duration, color_masks):
    # TODO: iterate over the audio file
    # TODO: more checks
    if len(n_fft) != 3:
        print("3 n_fft must be provided")
    res = np.zeros((299, int(299 * duration / 1.5), 3), dtype='uint8')
    for i, fft in enumerate(n_fft):
        im = create_spectrogram(
            sample,
            duration=duration,
            n_fft=fft,
            contrast=1.5,
            color_mask=color_masks[i])
        ia = np.asarray(im)
        res = res + ia
    composite = Image.fromarray(res, mode='RGB')
    return composite
