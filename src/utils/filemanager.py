import logging
import os
import re
import zipfile
from datetime import datetime
from glob import glob

import pandas as pd
from utils.wav_headers import get_wav_headers
from wac2wav import wac2wav

RECORDER_AM = "Audiomoth"
RECORDER_SM2 = "SongMeter"
RECORDER_ES = "Ecosongs"
RECORDER_AUTO = "Auto-detect"


class FileManager:
    """Class to manage file import. Works with

    Attributes
    ----------
    options : type
        Description of attribute `options`.
    archive : type
        Description of attribute `archive`.
    FILE_EXT : type
        Description of attribute `FILE_EXT`.

    """
    # TODO: put in config
    FILE_EXT = (".wac", ".wav", ".WAV")
    # TODO: put in config
    PATTERNS = {"Audiomoth": "([A-F0-9]{8})", "SongMeter": "(.+)_(\d{8}_\d{6})"}

    def __init__(self, sites=None):
        self.sites = sites
        self.root_dir = ""
        self.dest_dir = ""
        self.compress_old = False
        self.file_paths = ""
        self.to_wav = None
        self.archive = None
        self.options = {"recursive": True, "recorder": None, "folder": False}
        self.regex = {key: re.compile(value) for (key, value) in self.PATTERNS.items()}

    def log(self, text):
        print(text)

    def get_files(self):
        if self.options["folder"]:
            self.get_files_from_folder()
        self.extract_infos()
        self.files_loaded()
        return self.file_infos

    def get_files_from_folder(self):
        self.log("get files from folder: " + self.root_dir)
        pattern = self.root_dir
        if self.options["recursive"]:
            pattern += "/**"
        files = []
        for ext in self.FILE_EXT:
            pattrn = pattern + "/*" + ext
            files.extend(glob(pattrn, recursive=True))
        self.file_paths = files

    def get_files_to_convert(self):
        df = self.file_infos
        self.to_wav = df.loc[df.ext == "wac", 'path'].tolist()
        if self.to_wav:
            print(self.to_wav)

    def files_loaded(self):
        self.log("\n".join(self.file_paths))

    def extract_infos(self):
        file_infos = list(map(self.extract_info, self.file_paths))
        # TODO: oder of columns in config
        self.file_infos = pd.DataFrame(file_infos)
        self.log(self.file_infos)

    def recorder_from_name(self, file, path):
        for key, reg in self.regex.items():
            m = reg.match(file)
            if m:
                return(key, m)

    def extract_date(self, recorder, match):
        return getattr(self, "extract_date_" + recorder.lower())(match)

    def extract_date_audiomoth(self, match):
        date = datetime.fromtimestamp(int(int(match.group(1), 16)))
        logging.debug("extracting date AM: " + str(date))
        return date

    def extract_date_songmeter(self, match):
        date = datetime.strptime(match.group(2), "%Y%m%d_%H%S%M")
        logging.debug("extracting date SM2: " + str(date))
        return date

    def extract_info(self, fullpath):
        # Initialize result dict. Defaults added for table display
        logging.debug("Extracting information from: " + fullpath)
        res = {"error": 0, "site": None, "plot": None, "date": None,
               "year": None, "name": None, "path": fullpath, "recorder": None}

        # Split path and reverse it
        path = fullpath.split("/")
        path.reverse()

        # Get file name
        file = path[0]
        res["old_name"] = file
        # Get extension
        f = file.split(".")
        name = ''.join(f[:len(f) - 1])
        res["ext"] = f[len(f) - 1].lower()

        # Detect recorder based on pattern matching
        match = None
        if self.options["recorder"] != RECORDER_AUTO:
            recorder = self.options["recorder"]
            match = self.regex[recorder].match(name)
        else:
            recorder, match = self.recorder_from_name(name, os.path.dirname(fullpath))

        res["date"] = self.extract_date(recorder, match)
        res["recorder"] = recorder

        # Split file using underscore: only for difference between Audiomoth
        # and SongMeter
        # TODO: change if add support for other recorders and normal audio files
        # use pattern matching
        # data = name.split("_", 1)
        # # TODO: add constants
        # if self.options["recorder"] == "Auto-detect":
        #     if len(data) == 1:
        #         res["recorder"] = "Audiomoth"
        #     else:
        #         res["recorder"] = "SongMeter"
        # else:
        #     res["recorder"] = self.options["recorder"]

        # TODO: validate info extraction
        # Get data from folder hierarchy (only valid for folder import)
        # Only retrieve info from path hierarchy if indexes fit
        # TODO : catch errors on folder hierarchy
        if self.options["folder_hierarchy"]:
            if len(path) < 4:
                error = "Cannot extrapolate information from hierarchy, not enough folders"
            else:
                res["site"] = path[self.options["site_info"]["site"]]
                res["year"] = path[self.options["site_info"]["year"]]
                res["plot"] = path[self.options["site_info"]["plot"]]
        else:
            res["site"] = self.options["site_info"]["site"]
            res["year"] = self.options["site_info"]["year"]
            res["plot"] = self.options["site_info"]["plot"]

        # site_name = res["site"]
        # if self.sites is not None:
        #     tmp = self.sites.loc[self.sites["Site"] == res["site"], "Abbreviation"]
        #     if not tmp.empty:
        #         site_name = tmp.item()

        # TODO: extract info from wav header
        res["name"] = (res["plot"]
                       + "_" + res["date"].strftime('%Y-%m-%d_%H:%M:%S'))
        res["duration"] = 0
        res["sample_rate"] = 0

        if (res["ext"] == "wav"):
            headers = get_wav_headers(fullpath)
            res["duration"] = headers["Duration"]
            res["sample_rate"] = headers["SampleRate"]

        return(res)

    # TODO: set options as arguments like everywhere else
    def set_args(self, dest="", compress_old=True):
        self.dest_dir = dest
        self.compress_old = compress_old
        # Only compile regex if we need to move
        if dest:
            self.regex = re.compile(r"^" + self.root_dir + "(.*)\.wac$")

    def open_archive(self, filename="backup_wac.zip"):
        if self.compress_old and self.root_dir:
            self.archive = zipfile.ZipFile(self.root_dir + "/" + filename, 'w')

    def close_archive(self):
        if self.archive:
            self.archive.close()

    def files_to_wav(self, files):
        for filename in files:
            self.file_to_wav(filename)

    def file_to_wav(self, filename):
        if self.dest_dir:
            new = self.regex.sub(self.dest_dir + "\\1.wav", filename)
            dirname = os.path.dirname(new)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        else:
            new = filename.replace(".wac", ".wav")
        self.log("Converting {0} in {1}".format(filename, new))
        wac2wav(filename, new)

        # Update file info with information about the wav file
        headers = get_wav_headers(new)
        mask = self.file_infos.path == filename
        cols = ["duration", "sample_rate", "path", "ext"]
        self.file_infos.loc[mask, cols] = [headers["Duration"], headers["SampleRate"], new, "wav"]

        if self.archive:
            print("adding file to archive")
            self.archive.write(filename, filename.replace(self.root_dir, ""))

    def remove_files(self):
        self.log("removing files")
        for fn in self.files:
            os.remove(fn)

    def rename_file_tuple(self, tuple):
        (old, new) = tuple
        if old != new:
            # TODO: error catching
            os.rename(old, new)
            mask = self.file_infos.path == old
            self.file_infos.loc[mask, "path"] = new
