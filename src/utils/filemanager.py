import os
from datetime import datetime
from glob import glob


class FileManager:
    # TODO: put in config
    FILE_EXT = (".wac", ".wav", ".WAV")

    def __init__(self, type=None, subfolders=True):
        self.type = type

    def wac2wav(self, path):
        pass

    def wac2flac(self, path):
        pass

    def set_files(self, files):
        # TODO Extract metatdata here?
        self.files = files
        self.root_dir = os.path.dirname(files[0])

    def get_all_files(self, recursive=True):
        pattern = self.root_dir
        if recursive:
            pattern += "/**"
        files = []
        for ext in self.FILE_EXT:
            pattrn = pattern + "/*" + ext
            print(pattrn)
            files.extend(glob(pattrn, recursive=True))
        self.files = files

    def extract_info(files):
        pass

    def extract_metadata(fullpath, type=None, use_hierarchy=True,
                         folder_idx={"plot": 1, "site": 2, "year": 3},
                         site_infos={"plot": None, "site": None, "year": None}):
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
        # NOTE: might need to change if add support for other recorder
        data = name.split("_", 1)
        if type is None and len(data) == 1:
            res["type"] = "Audiomoth"
        else:
            res["type"] = "SongMeter"
        res["type"] = type

        # Extract date for all types
        if type == "Audiomoth":
            res["date"] = datetime.fromtimestamp(
                int(int(data[0], 16))
            )
        elif type == "SongMeter":
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
