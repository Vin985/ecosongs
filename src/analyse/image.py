import functools
import itertools
import json

import numpy as np
import webcolors
from PIL import Image, ImageEnhance, ImageOps


class ImageGenerator:
    def __init__(self, config):
        self.__read_config(config)

    def __read_config(self, config):
        # TODO: add parent class?
        for key in config:
            setattr(self, key, config[key])
        self.color_masks = [self.__get_color_rgb(col) for col in self.color_masks_str]

    def __get_color_rgb(self, color):
        if type(color) is tuple:
            return (color)
        elif type(color) is str:
            return (webcolors.name_to_rgb(color))

    # Prepare spectrograms to generate image
    def __prepare_spectrogram(self, spec):
        # Make sure spectrogram is in float32 because pillow doesn't
        # support float64
        spec = spec.astype("float32")
        # Normalize spectrogram in [0:1]
        # TODO: use librosa normalize?
        min = spec.min(axis=None)
        max = spec.max(axis=None)
        spec -= min
        spec /= (max - min)
        print(self.invert_colors)
        if self.invert_colors:
            spec = 1 - spec
        spec = spec * 255
        # flip upside down since writing image start from top left
        spec = np.flipud(spec)
        return spec

    def spec2img(self,
                 spec,
                 color_mask=(255, 0, 0),
                 size=None,
                 resize_method=Image.BILINEAR):

        spec = self.__prepare_spectrogram(spec)

        # Create image from float points
        img = Image.fromarray(spec, mode='F')
        # Convert in grayscale
        img = img.convert("L")
        # Colorise spectrogram
        if color_mask:
            img = ImageOps.colorize(img, (0, 0, 0), color_mask)

        # enhance contrast
        if self.contrast:
            if self.contrast == -1:
                img = ImageOps.autocontrast(img)
            else:
                c_enh = ImageEnhance.Contrast(img)
                img = c_enh.enhance(self.contrast)

        if size is not None:
            img = img.resize(size, resize_method)

        return img

    def create_composite_part(self, spec, color_mask):
        img = self.spec2img(
            spec.spec, color_mask, size=(int(299 * spec.duration / 1.5), 299))
        return np.asarray(img)

    def generate_composite(self, sample, specgen):
        # TODO: more checks
        if len(self.composite_ffts) != 3:
            print("3 spectrograms sizes must be provided in the "
                  " composite_ffts option in the configuration file")
            return ()
        specs = [
            specgen.create_spectrogram(sample, fft)
            for fft in self.composite_ffts
        ]
        res = itertools.starmap(self.create_composite_part,
                                zip(specs, self.color_masks))
        res = functools.reduce(np.add, res)
        composite = Image.fromarray(res, mode='RGB')
        return composite
