#%%

import datetime
import random
from pathlib import Path


import pandas as pd

from pysoundplayer.audio import Audio


SELECTED_PLOT = "IGLO_B"
SELECTED_YEAR = "2018"

START_DATE = datetime.date(2018, 6, 11)
END_DATE = datetime.date(2018, 7, 23)

DEST_DIR = (
    Path(
        "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Arctic/Christine/full_summer/"
    )
    / SELECTED_YEAR
    / SELECTED_PLOT
)

DURATION = 30

all_recordings = pd.read_feather(
    "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db/feather/recordings_all.feather"
)


recs = all_recordings.loc[
    (all_recordings["plot"] == SELECTED_PLOT)
    & (all_recordings["year"] == SELECTED_YEAR)
]

recs = recs.loc[(recs.date.dt.date >= START_DATE) & (recs.date.dt.date <= END_DATE)]

recs["day"] = recs.date.dt.dayofyear
recs["hour"] = recs.date.dt.hour
recs = recs.sort_values("date")


#%%


def get_random_extract(src_path, dest_dir, duration, name=None):
    audio = Audio(src_path, sr=None, mono=True)
    if not name:
        name = str(src_path.stem)
    if audio.duration >= duration:
        start = random.randint(1, audio.duration - duration)
        audio_dest_path = dest_dir / "{}_{}.wav".format(name, start)
        if not audio_dest_path.exists():
            print("Writing file {} starting at {} sec".format(audio_dest_path, start))
            end = min(start + duration, audio.duration)
            extract = audio.get_extract(start, end, seconds=True)
            audio_dest_path.parent.mkdir(parents=True, exist_ok=True)
            audio.write(str(audio_dest_path), data=extract, sr=audio.sr)


previous_day = 0
previous_hour = 0
previous_subset = 0
subset = "subset_"

for row in recs.itertuples():
    try:
        # * We are in the same day and hour
        if row.day == previous_day and row.hour == previous_hour:
            subset_nb = 1 if previous_subset == 2 else 2
        else:
            # * select subset randomly
            subset_nb = random.randint(1, 2)
        dest_dir = DEST_DIR / (subset + str(subset_nb))
        get_random_extract(Path(row.path), dest_dir, DURATION, name=row.name)
        previous_subset = subset_nb
        previous_day = row.day
        previous_hour = row.hour
    except Exception:
        print("Error while processing file ", row.path)
