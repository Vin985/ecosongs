import os
from datetime import datetime
from glob import glob

import pandas as pd

RECORDER_AM = "Audiomoth"
RECORDER_SM2 = "SongMeter"
RECORDER_AUTO = "Auto-detect"


class FileManager:
    # TODO: put in config
    FILE_EXT = (".wac", ".wav", ".WAV")

    def __init__(self, recorder=None, recursive=True):
        self.options = {"recursive": recursive, "recorder": recorder}

    def log(self, text):
        print(text)

    def wac2wav(self, path):
        pass

    def wac2flac(self, path):
        pass

    def get_files(self):
        if self.options["folder"]:
            self.get_files_from_folder()
        self.extract_infos()
        self.files_loaded()

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

    def set_overwrite(self):
        pass
        # self.file_manager.overwrite = self.checkbox_overwrite.isChecked()

    def set_root(self, path):
        pass
        # self.file_manager.root_dir = path

    def set_dest(self, path):
        pass
        # self.file_manager.dest_dir = path

    def extract_infos(self):
        file_infos = list(map(self.extract_info, self.file_paths))
        # TODO: oder of columns in config
        self.file_infos = pd.DataFrame(file_infos, columns=["name", "year", "site", "plot", "date", "path", "ext", "recorder", "error"])
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
        res["ext"] = f[len(f) - 1]
        # Get filename
        name = f[0]
        # Split file using underscore: only for difference between Audiomoth
        # and SongMeter
        # NOTE: might need to change if add support for other recorders
        data = name.split("_", 1)
        # TODO: add constants instead of
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

        res["name"] = res["site"] + res["plot"] + \
            res["date"].strftime('%Y-%m-%d_%H:%M:%S')
        return(res)

    def extract_metadata(fullpath, recorder=None, use_hierarchy=True,
                         folder_idx={"plot": 1, "site": 2, "year": 3},
                         site_infos={"plot": None, "site": None, "year": None}):
        # TODO: use data sources for file location to save path
        # Initialize result dict. Defaults added for table display
        res = {"error": 0, "site": None, "plot": None,
               "year": None, "name": None, "path": fullpath}
        # Remove root directory to deduce info from hierarchy
        path = fullpath.split("/")
        path.reverse()
        path = path[0:2]
        print(path)

        # Separate filename from extension
        file = path[0]
        f = file.split(".")
        res["ext"] = f[len(f) - 1]
        # Get filename
        name = f[0]
        # Split file using underscore: only for difference between Audiomoth
        # and SongMeter
        # NOTE: might need to change if add support for other recorders
        data = name.split("_", 1)
        if recorder is None and len(data) == 1:
            res["recorder"] = "Audiomoth"
        else:
            res["recorder"] = "SongMeter"
        res["recorder"] = recorder

        # Extract date for all recorders
        if recorder == "Audiomoth":
            res["date"] = datetime.fromtimestamp(
                int(int(data[0], 16))
            )
        elif recorder == "SongMeter":
            res["date"] = datetime.strptime(data[1], "%Y%m%d_%H%S%M")

        # TODO: validate info extraction
        # Get data from folder hierarchy (only valid for folder import)
        # Only retrieve info from path hierarchy if indexes fit
        if use_hierarchy:
            res["site"] = path[folder_idx["site"]]
            res["year"] = path[folder_idx["year"]]
            res["plot"] = path[folder_idx["plot"]]
        else:
            if all(site_infos.values()):
                res["site"] = path[folder_idx["site"]]
                res["year"] = path[folder_idx["year"]]
                res["plot"] = path[folder_idx["plot"]]

        res["name"] = res["site"] + res["plot"] + \
            res["date"].strftime('%Y-%m-%d_%H:%M:%S')

        return(res)


# convert batch from wac to wav

# convert wav to flac?

# create database
