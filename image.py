import functools
import itertools

import numpy as np
from PIL import Image, ImageEnhance, ImageOps


class ImageGenerator:
    def __init__(self, config):
        self.config = config

    # Prepare spectrograms to generate image
    def __prepare_spectrogram(self, spec):
        # Make sure spectrogram is in float32 because pillow doesn't
        # support float64
        spec = spec.astype("float32")
        # Normalize spectrogram in [0:1]
        spec -= spec.min(axis=None)
        spec /= spec.max(axis=None)
        if (self.config['invert_colors']):
            spec = 1 - spec
        spec = spec * 255
        # flip upside down since writing image start from top left
        spec = np.flipud(spec)
        return spec

    def spec2img(self, spec, color_mask):

        # spec = librosa.amplitude_to_db(spec, ref=np.max, top_db=80.0)
        spec = self.__prepare_spectrogram(spec)

        # Create image from float points
        img = Image.fromarray(spec, mode='F')
        # Convert in grayscale
        img = img.convert("L")
        # Colorise spectrogram
        img = ImageOps.colorize(img, (0, 0, 0), color_mask)

        # enhance contrast
        if (self.config['contrast'] > 0):
            c_enh = ImageEnhance.Contrast(img)
            img = c_enh.enhance(self.config['contrast'])

        return img

    def create_composite_part(self, spec, color_mask):
        img = self.spec2img(spec.spec, color_mask)
        img = img.resize((int(299 * spec.duration / 1.5), 299), Image.BILINEAR)
        return np.asarray(img)

    def generate_composite(self, specs):
        # TODO: iterate over the audio file
        # TODO: more checks
        if len(specs) != 3:
            print("3 spectrograms must be provided")
        res = itertools.starmap(self.create_composite_part,
                                zip(specs, self.config['color_masks']))
        res = functools.reduce(np.add, res)
        composite = Image.fromarray(res, mode='RGB')
        return composite
