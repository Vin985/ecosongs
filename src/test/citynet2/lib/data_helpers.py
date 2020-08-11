import pandas as pd
import librosa
import os
import yaml

# base = yaml.load(open("CONFIG.yaml"), Loader=yaml.Loader)["base_dir"]
# labels_dir = base + "/annotations/"
# wav_dir = base + "/wavs/"

HUMAN_NOISES = set(
    [
        "mix traffic",
        "braking",
        "voices",
        "electrical",
        "anthropogenic unknown",
        "airplane",
        "beep",
        "metal",
        "bus emitting",
        "footsteps",
        "mower",
        "whistle",
        "siren",
        "coughing",
        "music",
        "horn",
        "startthecar",
        "bells",
        "applause",
        "dog bark",
        "road traffic",
        "braking vehicle (road or rail)",
        "human voices",
        "mechanical",
        "vehicle horn (road or rail)",
        "air traffic",
        "vehicle alarm",
        "human voice",
        "machinery",
        "church bell",
        "breaking vehicle",
        "deck lowering",
        "car horn",
        "rail traffic",
        "alarm",
        "vehicle horn",
        "building ventilation system",
        "car alarm",
        "rock",
        "church bells",
        "train horn",
        "mobile phone",
        "train station announcement",
        "hammering",
        "door opening",
        "dog barking",
        "vehicle breaking",
        "cat",
        "glass into bins",
        "barking dog",
        "television",
        "sweeping broom",
        "ball bouncing",
        "bat hitting ball",
        "laughing",
        "clapping",
        "camera",
        "train doors (beeping)",
        "lawnmower",
    ]
)

ANIMAL_NOISES = set(
    [
        "bird",
        "wing beats",
        "bat",
        "fox",
        "grey squirrel",
        "invertebrate",
        "insect",
        "animal",
        "wings beating",
        "russling leaves (animal)",
        "amphibian",
        "squirrel",
        "russling vegetation (animal)",
    ]
)

OTHER = set(
    [
        "rain",
        "unknown sound",
        "electrical disturbance",
        "vegetation",
        "wind",
        "unknown",
        "metalic sound",
        "dripping water",
        "shower",
        "metalic",
        "rubbish bag",
        "water dripping",
        "water splashing",
        "rainfall on vegetation",
    ]
)


def load_annotations(fname, audio_dir, labels_dir):

    # load file and convert to spectrogram
    wav, sample_rate = librosa.load(audio_dir + fname, None)

    # create label vector...
    biotic = 0 * wav
    anthropogenic = 0 * wav

    csv_fname = labels_dir + fname.replace(".wav", "-sceneRect.csv")
    print("Loading annotations for file: " + fname)
    if os.path.exists(csv_fname):
        pd_annots = pd.read_csv(csv_fname, skip_blank_lines=True)
        # loop over each annotation...
        tmp = pd_annots.loc[~pd_annots.Filename.isna()]
        for _, annot in tmp.iterrows():
            # fill in the label vector
            start_point = int(float(annot["LabelStartTime_Seconds"]) * sample_rate)
            end_point = int(float(annot["LabelEndTime_Seconds"]) * sample_rate)

            label = annot["Label"].lower()
            if label in HUMAN_NOISES:
                anthropogenic[start_point:end_point] = 1
            elif label in ANIMAL_NOISES:
                biotic[start_point:end_point] = 1
            elif label in OTHER:
                pass
            else:
                raise Exception("Unknown label ", annot["Label"])
    else:
        pd_annots = pd.DataFrame()
        print("Warning - no annotations found for %s" % fname)

    return {"anthrop": anthropogenic, "biotic": biotic}, wav, sample_rate
