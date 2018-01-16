import configparser
import json

import webcolors


class Config:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path)
        self.__spectrogram_conf(config)
        self.__image_conf(config)

    def __spectrogram_conf(self, config):
        self.spectrogram = {}

        self.spectrogram['window'] = config.get("spectrogram", "window")
        self.spectrogram['default_fft'] = config.getint(
            "spectrogram", "default_fft", fallback=512)
        # noise removal parameters
        self.spectrogram['remove_noise'] = config.getboolean(
            "noise_removal", "remove_noise")
        self.spectrogram['window_smoothing'] = config.getint(
            "noise_removal", "window_smoothing")
        self.spectrogram['hist_rel_size'] = config.getint(
            "noise_removal", "hist_rel_size")

    def __image_conf(self, config):
        self.image = {}
        colors = json.loads(
            config.get(
                "image", "color_masks", fallback='["red", "lime", "blue"]'))
        self.image['color_masks'] = list(map(self.get_color_rgb, colors))
        self.image['contrast'] = config.getint("image", "contrast", fallback=0)
        self.image['invert_colors'] = config.getboolean(
            "image", "invert_colors", fallback=False)
        self.image['composite_ffts'] = json.loads(
            config.get("image", "composite_ffts"))

    def get_color_rgb(self, color):
        if type(color) is tuple:
            return (color)
        elif type(color) is str:
            return (webcolors.name_to_rgb(color))
