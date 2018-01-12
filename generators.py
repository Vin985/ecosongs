import json

import librosa
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

from compute_indice import remove_noiseInSpectro


class ImageGenerator:
    def __init__(self, config):
        self.color_masks = json.loads(config.get("image", "color_masks"))
        self.contrast = config.getint("image", "contrast")

        self.specgen = SpectrogramGenerator(config)

    # Prepare spectrograms to generate image
    def __prepare_spectrogram(self, spec, invert=False):
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

    def __spec2img(self,
                   spec,
                   color_mask=(255, 0, 0),
                   show=False,
                   save=False,
                   contrast=1,
                   invert_colors=False):

        # spec = librosa.amplitude_to_db(spec, ref=np.max, top_db=80.0)
        spec = self.__prepare_spectrogram(spec, invert=invert_colors)

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

    def create_image(self, sample, n_fft, show=False):
        spec = self.specgen.create_spectrogram(sample, n_fft)
        img = self.__spec2img(spec)
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


class SpectrogramGenerator:
    def __init__(self, config):
        # spectrogram parameters
        self.spec_window = config.get("spectrogram", "window")

        # noise removal parameters
        self.remove_noise = config.getboolean("noise_removal", "remove_noise")
        self.window_smoothing = config.getint("noise_removal",
                                              "window_smoothing")
        self.hist_rel_size = config.getint("noise_removal", "hist_rel_size")

    def create_spectrogram(self, sample, n_fft):
        spectro = librosa.stft(sample, n_fft, window=self.spec_window)
        mag, phase = librosa.magphase(spectro)

        specdb = librosa.amplitude_to_db(spectro, ref=np.max)
        if (self.remove_noise):
            specdb = remove_noiseInSpectro(
                specdb,
                histo_relative_size=self.hist_rel_size,
                window_smoothing=self.window_smoothing)
            specdb = specdb.astype("float32")

        return specdb
