import os.path
from datetime import datetime


class AudioExtract:
    def __init__(self, audio, sr):
        self.audio = audio
        self.sr = sr
        self.length = len(self.audio)
        self.duration = round(self.length / sr, 2)


class ExtractInfo:
    def __init__(self, path, audio_type):
        filename = os.path.basename(path)
        infos = filename.split(".")
        self.name = infos[0]
        self.ext = infos[1].lower()
        if audio_type is "songmeter":
            self.__extract_SM_info(infos[0])
        else:
            self.id = infos[0]
            self.date = "Unknown"

    # SongMeter format:
    # SITEID_DATE_TIME
    # SITEID : str
    # DATE: YYYYMMDD
    # TIME: HHMMSS
    def __extract_SM_info(self, path):
        res = path.split("_", 1)
        self.id = res[0]
        self.date = datetime.strptime(res[1], "%Y%m%d_%H%S%M")

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return (string)
