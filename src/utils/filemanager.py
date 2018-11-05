import logging
import os
import re
import zipfile
from datetime import datetime

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
    FILE_EXT = ("wac", "wav")
    # TODO: put in config
    PATTERNS = {"Audiomoth": "([A-F0-9]{8})",
                "SongMeter": "(.+)_(\d{8}_\d{6})",
                "Ecosongs": "(.+)_(.+)_(\d{4}-\d{2}-\d{2})_(\d{2}:\d{2}:\d{2})"}

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
            file_infos = self.get_files_from_folder()
        else:
            file_infos = self.extract_infos(None, self.file_paths)
        file_infos = list(filter(None, file_infos))
        print(file_infos)
        self.file_infos = pd.DataFrame(file_infos)
        self.files_loaded()
        return self.file_infos

    def get_files_from_folder(self):
        self.log("Retrieving files from folder: " + self.root_dir)
        # Listing all files and folders in root directory
        file_infos = []
        for (dirpath, dirnames, filenames) in os.walk(self.root_dir):
            # if files are present
            if filenames:
                # TODO: check for a conf file in order to update configurations
                if (os.path.exists("info.txt")):
                    print("file exists")
                # TODO add extra information
                # extract information from files
                file_infos += self.extract_infos(dirpath, filenames)
            if not self.options["recursive"]:
                break
        return file_infos

    def get_files_to_convert(self):
        df = self.file_infos
        self.to_wav = df.loc[df.ext == "wac", 'path'].tolist()
        if self.to_wav:
            print(self.to_wav)

    def files_loaded(self):
        self.log("\n".join(self.file_paths))

    def extract_infos(self, path, files):
        file_infos = [self.extract_info(path, file) for file in files]
        return file_infos

    def extract_info(self, dirpath, file):
        if not dirpath:
            # Path to parent drectory not provided, extract it from filename
            fullpath = file
            dirpath = os.path.dirname(file)
            file = os.path.basename(file)
        else:
            fullpath = os.path.join(dirpath, file)

        # Initialize result dict. Defaults added for table display
        self.log("Extracting information from: " + fullpath)

        # Get extension
        f = file.split(".")
        ext = f[len(f) - 1].lower()
        # Check if file is a supported audio file
        if ext not in self.FILE_EXT:
            logging.warning("File is not a supported audio file")
            return
        # Get name
        name = ''.join(f[:len(f) - 1])

        res = {"error": 0, "site": None, "plot": None, "date": None,
               "year": None, "name": None, "path": fullpath, "recorder": None}
        res["ext"] = ext
        res["old_name"] = file

        # Split path and reverse it
        path = dirpath.split("/")
        path.reverse()

        # Detect recorder based on pattern matching
        match = None
        if self.options["recorder"] != RECORDER_AUTO:
            recorder = self.options["recorder"]
            match = self.regex[recorder].match(name)
        else:
            recorder, match = self.recorder_from_name(name, dirpath)

        res["date"] = self.extract_date(recorder, match)
        res["recorder"] = recorder

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

        res["name"] = (res["plot"]
                       + "_" + res["date"].strftime('%Y-%m-%d_%H:%M:%S'))
        res["duration"] = 0
        res["sample_rate"] = 0

        if (res["ext"] == "wav"):
            headers = get_wav_headers(fullpath)
            if headers:
                res["duration"] = headers["Duration"]
                res["sample_rate"] = headers["SampleRate"]
            else:
                # TODO: add an error instead?
                return None

        return(res)

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
