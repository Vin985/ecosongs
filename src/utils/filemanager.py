import os
import re
import zipfile
from datetime import datetime
from glob import glob

import pandas as pd
from wac2wav import wac2wav

from audio.recording import Recording

RECORDER_AM = "Audiomoth"
RECORDER_SM2 = "SongMeter"
RECORDER_AUTO = "Auto-detect"


class FileManager:
    # TODO: put in config
    FILE_EXT = (".wac", ".wav", ".WAV")

    def __init__(self, recorder=None, recursive=True, sites=None):
        if sites:
            # TODO: load on demand!
            self.sites = pd.read_csv(sites, sep=";")
        else:
            self.sites = None
        self.options = {"recursive": recursive, "recorder": recorder}
        self.archive = None

    def log(self, text):
        print(text)

    def get_files(self):
        if self.options["folder"]:
            self.get_files_from_folder()
        self.extract_infos()
        self.files_loaded()
        return self.file_infos

    def get_files_to_convert(self):
        df = self.file_infos
        self.to_wav = df.loc[df.ext == "wac", 'path'].tolist()
        if self.to_wav:
            print(self.to_wav)

    def files_loaded(self):
        self.log("\n".join(self.file_paths))

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

    def extract_infos(self):
        file_infos = list(map(self.extract_info, self.file_paths))
        # TODO: oder of columns in config
        self.file_infos = pd.DataFrame(file_infos)
        self.log(self.file_infos)

    def extract_info(self, fullpath):
        # Initialize result dict. Defaults added for table display
        res = {"error": 0, "site": None, "plot": None,
               "year": None, "name": None, "path": fullpath}
        # Remove root directory to deduce info from hierarchy
        path = fullpath.split("/")
        path.reverse()
        path = path[0:4]

        # Separate filename from extension
        file = path[0]
        f = file.split(".")
        res["ext"] = f[len(f) - 1].lower()
        res["old_name"] = ''.join(f[:len(f) - 1])

        # Get filename
        name = f[0]
        # Split file using underscore: only for difference between Audiomoth
        # and SongMeter
        # TODO: change if add support for other recorders and normal audio files
        # use pattern matching
        data = name.split("_", 1)
        # TODO: add constants
        if self.options["recorder"] == "Auto-detect":
            if len(data) == 1:
                res["recorder"] = "Audiomoth"
            else:
                res["recorder"] = "SongMeter"
        else:
            res["recorder"] = self.options["recorder"]

        # Extract date for all recorders
        if res["recorder"] == "Audiomoth":
            res["date"] = datetime.fromtimestamp(
                int(int(data[0], 16))
            )
        elif res["recorder"] == "SongMeter":
            res["date"] = datetime.strptime(data[1], "%Y%m%d_%H%S%M")

        # TODO: validate info extraction
        # Get data from folder hierarchy (only valid for folder import)
        # Only retrieve info from path hierarchy if indexes fit
        # TODO : catch errors on folder hierarchy
        if self.options["folder_hierarchy"]:
            res["site"] = path[self.options["site_info"]["site"]]
            res["year"] = path[self.options["site_info"]["year"]]
            res["plot"] = path[self.options["site_info"]["plot"]]
        else:
            res["site"] = self.options["site_info"]["site"]
            res["year"] = self.options["site_info"]["year"]
            res["plot"] = self.options["site_info"]["plot"]

        site_name = res["site"]
        if self.sites is not None:
            tmp = self.sites.loc[self.sites["Site"] == res["site"], "Abbreviation"]
            if not tmp.empty:
                site_name = tmp.item()

        # TODO: extract info from wav header
        res["name"] = (site_name + "_" + res["plot"]
                       + "_" + res["date"].strftime('%Y-%m-%d_%H:%M:%S'))

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
            os.rename(old, new)
