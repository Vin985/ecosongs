import datetime
from os import path


def extract_from_file(filepath, recorder):
    data = {}
    # Split path
    basename = path.basename(filepath)
    fsp = basename.split(".")
    filename = fsp[0]
    # get extension type
    data["type"] = fsp[1].lower()
    if recorder is "SM":
        extract_SM_metadata(data, filename)
    else:
        data["name"] = filename
        data["date"] = "Unknown"
    return data

# SongMeter format:
# SITEID_DATE_TIME
# SITEID : str
# DATE: YYYYMMDD
# TIME: HHMMSS


def extract_SM_metadata(self, filename):
    res = {}
    data = filename.split("_", 1)
    res["name"] = data[0]
    res["date"] = datetime.strptime(res[1], "%Y%m%d_%H%S%M")
