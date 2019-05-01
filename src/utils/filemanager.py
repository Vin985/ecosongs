import logging
import os
import re
import zipfile
from datetime import datetime
import traceback

import pandas as pd
from wac2wav import wac2wav

from utils.wav_headers import get_wav_headers

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
                "Ecosongs": "(.+)_(.+)_(\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2})"}

    def __init__(self, sites=None):
        self.file_infos = None
        # will be used to change site name to shortcut
        self.sites = sites
        self.root_dir = ""
        self.dest_dir = ""
        self.compress_old = False
        self.file_paths = ""
        self.to_wav = None
        self.archive = None
        self.options = {"recursive": True, "recorder": RECORDER_AUTO, "folder": False,
                        "site_info": {"site": 1, "year": 0, "plot": 2},
                        "folder_hierarchy": True}
        self.regex = {key: re.compile(value)
                      for (key, value) in self.PATTERNS.items()}

    def log(self, text):
        print(text)

    def get_infos(self):
        try:
            if self.options["folder"]:
                file_infos = self.get_from_folder()
            else:
                file_infos = self.extract_infos(None, self.file_paths)
            file_infos = list(filter(None, file_infos))
            self.file_infos = pd.DataFrame(file_infos)
            self.files_loaded()
            return self.file_infos
        except Exception:
            print(traceback.format_exc())

    def get_from_folder(self):
        self.log("Retrieving files from folder: " + self.root_dir)
        # Listing all files and folders in root directory
        file_infos = []
        for (dirpath, _, filenames) in os.walk(self.root_dir):
            # if files are present
            if filenames:
                # TODO: check for a conf file in order to update configurations
                if os.path.exists("info.txt"):
                    print("file exists")
                # TODO add extra information
                # extract information from files
                file_infos += self.extract_infos(dirpath, filenames)
            if not self.options["recursive"]:
                break
        return file_infos

    def extract_infos(self, path, files):
        file_infos = [self.extract_info(path, file) for file in files]
        return file_infos

    def extract_info(self, dirpath, file):
        # TODO split in smaller functions
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
            recorder, match = self.recorder_from_name(name)

        res["date"] = self.extract_date(recorder, match)
        res["recorder"] = recorder

        if self.options["folder_hierarchy"]:
            if len(path) < 4:
                # TODO: handle errors
                error = "Cannot extrapolate information from hierarchy, not enough folders"
            else:
                res["site"] = path[self.options["site_info"]["site"] - 1]
                res["year"] = path[self.options["site_info"]["year"] - 1]
                res["plot"] = path[self.options["site_info"]["plot"] - 1]
        else:
            res["site"] = self.options["site_info"]["site"]
            res["year"] = self.options["site_info"]["year"]
            res["plot"] = self.options["site_info"]["plot"]

        if res["date"]:
            res["name"] = (res["plot"] +
                           "_" + res["date"].strftime('%Y-%m-%d_%H:%M:%S'))
        else:
            res["name"] = name

        res["duration"] = 0
        res["sample_rate"] = 0

        if res["ext"] == "wav":
            headers = get_wav_headers(fullpath)
            if headers:
                res["duration"] = headers["Duration"]
                res["sample_rate"] = headers["SampleRate"]
            else:
                # TODO: add an error instead?
                return None

        return res

    def recorder_from_name(self, file):
        for key, reg in self.regex.items():
            m = reg.match(file)
            if m:
                return(key, m)
        logging.warning(
            "Name does not match any known recorder, skipping automatic detection")
        return (None, None)

    def extract_date(self, recorder, match):
        if not recorder:
            return None
        return getattr(self, "extract_date_" + recorder.lower())(match)

    def extract_date_audiomoth(self, match):
        date = datetime.fromtimestamp(int(int(match.group(1), 16)))
        logging.debug("extracting date AM: " + str(date))
        return date

    def extract_date_songmeter(self, match):
        date = datetime.strptime(match.group(2), "%Y%m%d_%H%M%S")
        logging.debug("extracting date SM2: " + str(date))
        return date

    def extract_date_ecosongs(self, match):
        date = datetime.strptime(match.group(3), "%Y-%m-%d_%H:%M:%S")
        logging.debug("extracting date Ecosongs: " + str(date))
        return date

    def get_files_to_convert(self):
        self.to_wav = list(self.file_infos.loc[self.file_infos.ext == "wac", [
            'path', 'old_name', 'name']].itertuples(index=False))
        print(self.to_wav)

    def files_loaded(self):
        self.log("\n".join(self.file_paths))

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

    def convert_files(self, files):
        for filename in files:
            self.convert_file(filename)

    def convert_file(self, filename):
        print("in converting")
        try:
            # TODO: add options to change audio type
            (path, old_name, new_name) = filename
            print(filename)
            new_path = self.get_new_path(path, old_name, new_name)

            new_path = new_path + ".wav"
            print(new_path)

            if self.dest_dir:
                # new_path = new_path.replace(self.root_dir, self.dest_dir)
                dirname = os.path.dirname(new_path)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)

            self.log("Converting {0} in {1}".format(path, new_path))
            wac2wav(path, new_path)

            # Update file info with information about the wav file
            if os.path.exists(new_path):
                headers = get_wav_headers(new_path)
                mask = self.file_infos.path == path
                cols = ["duration", "sample_rate", "path", "ext"]
                self.file_infos.loc[mask, cols] = [
                    headers["Duration"], headers["SampleRate"], new_path, "wav"]

            if self.archive:
                print("adding file to archive")
                self.archive.write(
                    filename, filename.replace(self.root_dir, ""))
        except Exception as e:
            print(traceback.format_exc())

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

    def get_new_path(self, path, old, new):
        new_path = path.replace(old, new)
        if self.dest_dir:
            new_path = new_path.replace(self.root_dir, self.dest_dir)
        return(new_path)

    def create_links(self, overwrite=True):
        cols = self.file_infos.loc[:, ["path", "old_name", "name"]]
        new_paths = [self.get_new_path(*row)
                     for row in cols.itertuples(index=False)]
        tmp = list(zip(self.file_infos.loc[:, "path"], new_paths))
        for old, new in tmp:
            self.log("Creating link " + new + " to " + old)
            if not os.path.exists(os.path.dirname(new)):
                os.makedirs(os.path.dirname(new))
            if (os.path.exists(new) and overwrite):
                self.log(new + " already exists. Overwriting!")
                os.remove(new)
            os.symlink(old, new)
