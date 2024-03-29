import configparser
import inspect
import os

import feather
import numpy as np
import pandas as pd
from plotnine import (aes, element_text, facet_grid, geom_bar, geom_histogram,
                      geom_point, geom_smooth, geom_text, ggplot, ggtitle,
                      position_dodge, scale_fill_discrete, scale_x_continuous,
                      scale_x_discrete, theme, theme_classic, xlab, ylab)


currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from plot.events_plot import EventsPlot
    from analysis.detection import predictions_utils
except Exception:
    print("Woops, module EventsPlot not found")


TAGS_ROOT_PATH = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
TAGS_LABELS_PATH = os.path.join(TAGS_ROOT_PATH, "labels")
INCLUDE_TAG = ["Biophony", "Bird"]
EXCLUDE_TAG = ["Human"]


PREDICTIONS_PATH = "../db/feather/activity_predictions.feather"
EVENTS_PATH = "../db/feather/song_events_good_bak_151119.feather"
RECORDINGS_PATH = "../db/feather/recordings.feather"
MATCHED_PATH = "matched_events.feather"

TAGS_COLUMNS = {"Filename": "file_name", "tags": "tags",
                "LabelStartTime_Seconds": "tag_start", "LabelEndTime_Seconds": "tag_end", "overlap": "overlap", "background": "background"}
TAGS_COLUMNS_TYPE = {"overlap": "str"}
PREDICTIONS_COLUMNS = {'end': "event_end", 'event_id': "event_id",
                       'recording_id': "recording_id", 'start': "event_start",
                       'name': "file_name", "index": "event_index"}
EVENTS_COLUMNS = {'end': "event_end", 'event_id': "event_id",
                  'recording_id': "recording_id", 'start': "event_start",
                  'name': "file_name", "index": "event_index", "event_duration": "event_duration"}
# SPECIES_LIST = ["AMGP", "SESA", "WRSA", "LALO", "UNKN", "Human", "Insect"]
# SPECIES_LABELS = {"AMGP": "American Golden Plover",
#                   "SESA": "Semipalmated Sandpiper",
#                   "WRSA": "White-rumped Sandpiper",
#                   "LALO": "Lapland Longspur",
#                   "UNKN": "Unknown",
#                   "Human": "Human",
#                   "Insect": "Insect"}
SPECIES_LIST = ["Shorebird", "LALO", "UNKN", "Human", "Insect"]
SPECIES_LABELS = {"Shorebird": "Shorebird",
                  "LALO": "Passerine",
                  "UNKN": "Unknown",
                  "Human": "Human",
                  "Insect": "Insect"}


def get_done_files(path):
    local_conf = os.path.join(path, "config.conf")
    done_files = []
    if os.path.isfile(local_conf):
        config = configparser.ConfigParser()
        config.read(local_conf)
        done_files = config['files'].get("files_done", [])
        if type(done_files) is str:
            done_files = done_files.split(",")
        # remove extension
        res = [f[:-4] for f in done_files]
    return res


def check_tags_columns(df, columns):
    if columns:
        if type(columns) is dict:
            df["tags"] = df["Label"] + \
                "," + df["Related"]
            df = df[columns.keys()]
            df = df.rename(columns=columns)
            df.file_name = df.file_name.apply(
                lambda x: x[:-4])
        else:
            raise ValueError(
                "columns must be a dict with old labels as keys and new labels as values")
    return df


def has_excluded_tags(df, filter_options):
    keep_by_default = filter_options.get("keep_by_default", False)
    has_tags = filter_options.get("has_tags", [])
    exclude_tags = filter_options.get("exclude_tags", [])
    res = not all(df.tags.apply(keep_tag, has_tags=has_tags,
                                exclude_tags=exclude_tags, keep_by_default=keep_by_default))
    # if not res:
    #     print(df)
    return res


def load_annotations(root_path, tags_path, only_done=True, columns=None, columns_type=None, extensions=[".csv"], filter_options=None):
    res_files = []
    dfs = []
    done_files = []
    res = pd.DataFrame()
    # Only get done files. Load list of done files
    if only_done:
        done_files = get_done_files(root_path)
    for root, dirs, files in os.walk(tags_path):
        for f in sorted(files):
            # do not check hidden files or locked files
            if not f[0] == ".":
                # Get extension
                ext = f[-4:]
                if ext in extensions:
                    file_id = f[:-14]
                    if (not only_done) or (only_done and (file_id in done_files)):
                        df = pd.read_csv(os.path.join(
                            tags_path, f), dtype=columns_type)
                        try:
                            df = check_tags_columns(df, columns)
                            if filter_options:
                                if has_excluded_tags(df, filter_options):
                                    continue
                        except KeyError as ke:
                            print("Key Error {0} found for file {1}. Skipping. Please make sure the file is correct and has all columns".format(
                                ke, file_id))
                            continue
                        dfs.append(df)
                        res_files.append(file_id)
        # only walk through the first level of the directory
        break
    if dfs:
        res = pd.concat(dfs, ignore_index=True)
        res["tag_duration"] = res["tag_end"] - res["tag_start"]
    return (res_files, res)


def detect_events(df, options):
    res = predictions_utils.detect_songs_events(df, df.name, options)
    return res


def get_events(predictions, options):
    events = predictions.groupby("recording_id", as_index=False).apply(
        detect_events, options)
    events.reset_index(inplace=True)
    events.drop(["level_0", "level_1"], axis=1, inplace=True)
    events["event_duration"] = events["end"] - \
        events["start"]
    return events


def prepare_events(events, recordings, columns):
    events = events.merge(
        recordings[["id", "name"]], left_on="recording_id", right_on="id")
    events.reset_index(inplace=True)
    events = events[columns.keys()]
    events.rename(columns=columns, inplace=True)
    return events


def load_recordings(recordings_path, file_list):
    recordings_data = feather.read_dataframe(recordings_path)
    recs_df = recordings_data.loc[recordings_data["name"].isin(
        file_list)]
    return recs_df


def load_predictions(predictions_path, recordings):
    # Load raw data
    predictions_data = feather.read_dataframe(predictions_path)
    predictions_df = predictions_data.loc[predictions_data.recording_id.isin(
        recordings)]
    return predictions_df


def merge_annotations(annots):
    res = []
    previous = {}
    annots.sort_values(by=['start'])
    for idx, annot in annots.iterrows():
        if not previous:
            previous = {"start": annot.start, "end": annot.end,
                        "duration": annot.duration, "n_annot": 1}
            res.append(previous)
        else:
            # Next annotation overlaps with the previous one
            if previous["start"] <= annot.start < previous["end"]:
                # annotation ends later than the previous one: use the end of this one instead
                if annot.end > previous["end"]:
                    # print("annotation overlap, extending the last one")
                    previous["end"] = annot.end
                    previous["n_annot"] += 1
                    previous["duration"] = previous["end"] - previous["start"]
            else:
                # Annotation starts after the next one, create new tag
                previous = {"start": annot.start,
                            "end": annot.end, "duration": annot.duration, "n_annot": 1}
                res.append(previous)
    res = pd.DataFrame(res)
    return res


def match_events(tag, events_df=None):
    # get tags that overlap with the detected event
    events_df = events_df.drop(["file_name", "recording_id"], axis=1)
    events = events_df.loc[(events_df.event_start < tag.tag_end) &
                           (events_df.event_end > tag.tag_start)]
    events.reset_index(inplace=True, drop=True)

    tmp = [tag]
    if events.shape[0] == 0:
        empty_event = pd.Series(
            {"event_end": 0, "event_id": -1, "event_start": 0,
             "event_index": -1, "event_duration": 0})
        events = pd.DataFrame([empty_event])
    else:
        for i in range(1, events.shape[0]):
            tmp.append(tag)
    tmp_df = pd.DataFrame(tmp)
    tmp_df.reset_index(inplace=True)
    tmp_df.rename(columns={"index": "tag_index"}, inplace=True)
    res = pd.concat([tmp_df, events], join="outer", axis=1)

    return res


def match_tags(filename, annots_df, events_df):
    res = {}
    annots = annots_df.loc[annots_df.file_name == filename]
    # Get events detected for the file
    events = events_df.loc[events_df.file_name == filename]
    # Match events with annotations
    res = [match_events(row, events) for _, row in annots.iterrows()]
    match = pd.concat(res)

    return match


def get_matches(events, tags, file_list, saved_file=""):
    if os.path.isfile(saved_file):
        match_df = pd.read_feather(saved_file)
    else:
        res = [match_tags(f, tags, events) for f in file_list]
        match_df = pd.concat(res)
    return match_df


def get_stats(match_df, events_df):
    # True pos: number of unique events that matched with a tag
    true_pos_events = len(
        match_df[match_df.event_index != -1].event_index.unique())
    true_pos_tags = len(
        match_df[match_df.event_index != -1].tag_index.unique())
    # False neg: number of tags that did not have a match
    false_neg = match_df[match_df.event_index == -1].shape[0]
    # Number of tags that are matched
    n_tags_matched = len(
        match_df.loc[match_df.event_index != -1].tag_index.unique())

    # Precision: TP / TP + FP
    precision = true_pos_events / events_df.shape[0]
    # Recall: TP / TP + FN
    recall = true_pos_tags / (true_pos_tags + false_neg)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return {"n_events": events_df.shape[0], "n_tags": len(match_df.tag_index.unique()),
            "true_positive_events": true_pos_events,
            "true_positive_tags": true_pos_tags,
            "false_negative": false_neg,
            "n_tags_matched": n_tags_matched,
            "precision": precision,
            "recall": recall, "F1_score": f1_score}


def get_tag_overlap(events, only_matched=False):
    res = {}
    n_events = events.shape[0]
    dur_overlap = 0

    tmp = events.sort_values(by=["event_start"])
    tag_duration = tmp.iloc[0].tag_duration

    if only_matched:
        # Only keep tags that have been matched
        tmp = tmp.loc[tmp["event_id"] != -1]
        # If no results, return nothing
        if tmp.shape[0] == 0:
            return
    # Iterate over events
    for _, event in tmp.iterrows():
        if not tag_duration:
            tag_duration = event.tag_duration

            # tmp["tag_duration"] = tag_duration
        if event["event_duration"] > 0:
            # There is no overlap of events, just add the duration overlapping with annotation
            dur_overlap += min(event.tag_end, event.event_end) - \
                max(event.tag_start, event.event_start)

    res["tag_id"] = tmp.iloc[0].tag_index
    res["file_name"] = tmp.iloc[0].file_name
    res["tag_duration"] = tmp.iloc[0].tag_duration
    res["n_events"] = n_events
    res["dur_overlap"] = dur_overlap
    res["prop_overlap"] = dur_overlap / tag_duration
    res["event_avg_duration"] = tmp["event_duration"].agg("mean")
    return pd.Series(res)


def get_tags_overlap(match_df):
    res = match_df.groupby(
        ["tag_index"], as_index=False).apply(get_tag_overlap)
    return res


def filter_tags(df, *args, **kwargs):
    return df.loc[df.tags.apply(keep_tag, *args, **kwargs)]


def keep_tag(raw_tags, has_tags=[], exclude_tags=[], keep_by_default=False):
    tags = raw_tags.split(",")
    exclude = any([tag in exclude_tags for tag in tags])
    if exclude:
        return False
    include = any([tag in has_tags for tag in tags])
    if include:
        return True
    return keep_by_default
    # for tag in tags:
    #     if tag in exclude_tags:
    #         return False
    #     if tag in has_tags:
    #         return True
    # return keep_by_default


def get_species(raw_tags, species):
    tags = raw_tags.split(",")
    for tag in tags:
        if tag in species:
            return tag
    return None


if __name__ == '__main__':

    split_file = "matched_events_split.feather"

    filter_opts = {"exclude_tags": EXCLUDE_TAG, "has_tags": INCLUDE_TAG}

    files_with_annots, tags_df = load_annotations(root_path=TAGS_ROOT_PATH,
                                                  tags_path=TAGS_LABELS_PATH,
                                                  only_done=True,
                                                  columns=TAGS_COLUMNS,
                                                  columns_type=TAGS_COLUMNS_TYPE,
                                                  filter_options=filter_opts)

    print(tags_df)
    recordings_df = load_recordings(RECORDINGS_PATH, files_with_annots)

    predictions_df = load_predictions(
        PREDICTIONS_PATH, recordings_df.id.unique())

    event_options = {"min_activity": 0.95,
                     "min_duration": 0.01,
                     "end_threshold": 0.1}
    events_df = get_events(predictions_df, event_options)
    events_df = prepare_events(events_df, recordings_df, EVENTS_COLUMNS)

    # if not os.path.isfile(split_file):
    matches_df = get_matches(events_df, tags_df, files_with_annots)
    matches_df.reset_index(inplace=True)
    #     matches_df.to_feather("matched_events_split.feather")
    # else:
    #     matches_df = feather.read_dataframe(split_file)

    # match_df = filter_tags(match_df, has_tags=["Bird"])

    tags_df["species"] = tags_df.tags.apply(get_species, species=SPECIES_LIST)

    total_stats = get_stats(matches_df, events_df)
    print(total_stats)

    # fg_matches = matches_df.loc[matches_df.background == False]
    # fg_stats = get_stats(fg_matches, events_df)
    # print(fg_stats)

    # bg_matches = matches_df.loc[matches_df.background == True]
    # bg_stats = get_stats(bg_matches, events_df)
    # print(bg_stats)

    # overlap = get_tags_overlap(matches_df)
    # overlap["log_tag_dur"] = np.log(overlap["tag_duration"])
    # print(overlap)

    # overlap["prop_overlap"].agg("mean")

    # tags_df.shape[0]

    # # import math
    # # from sklearn import linear_model
    # #
    # # # Create linear regression object
    # # regr = linear_model.LinearRegression()
    # # X = overlap["tag_duration"].values
    # # X = X.reshape(-1, 1)
    # #
    # # Y = overlap["prop_overlap"].values.reshape(-1, 1)
    # # Y
    # #
    # # # Train the model using the training sets
    # # regr.fit(X, Y)
    # # import matplotlib.pyplot as plt
    # #
    # # plt.scatter(X, Y,  color='black')
    # # plt.plot(X, regr.predict(X), color='blue', linewidth=3)
    # # plt.xticks(())
    # # plt.yticks(())
    # # plt.show()
    # #
    # # regr.score(X, Y)
    # #
    # # pd.DataFrame.hist(overlap, "tag_duration", bins=20)

    # ov_plot = ggplot(data=overlap, mapping=aes(
    #     x="np.log(tag_duration)", y="prop_overlap"))
    # ov_plot += geom_point()
    # print(ov_plot)

    # less_1s = overlap.loc[overlap["tag_duration"] < 1]
    # less_1s["prop_overlap"].agg("mean")
    # less_1s.shape[0] / overlap.shape[0]

    # more_1s = overlap.loc[overlap["tag_duration"] >= 1]
    # more_1s["prop_overlap"].agg("mean")
    # # vals = less_1s["prop_overlap"].value_counts(bins=5)

    # print(match_df)

    # plt = (ggplot(data=overlap, mapping=aes(x='tag_duration', y='n_events')) +
    #        geom_point())
    # plt.save("dur_nevents_nohuman.png")
    # #
    # # plt = (ggplot(data=overlap, mapping=aes(x='log_tag_dur', y='prop_overlap')) +
    # #        geom_point())
    # # plt.save("test_dur_propover.png")

    # #
    # # plt = (ggplot(data=less_1s, mapping=aes(x='prop_overlap', y="stat(width*density)*100")) +
    # #        geom_histogram(bins=5))
    # # plt.save("less1s_hist_nohuman.png")
    # # plt = (ggplot(data=more_1s, mapping=aes(x='prop_overlap', y="stat(width*density)*100")) +
    # #        geom_histogram(bins=5))
    # # plt.save("more1s_hist_nohuman.png")
    # tags_summary = tags_df.groupby(["species"]).agg(
    #     {"tag_duration": "sum", "species": "count"})
    # tags_summary.rename(columns={"species": "count"}, inplace=True)

    # tags_summary["tag_duration"] = tags_summary.tag_duration.astype(int)
    # tags_summary["duration"] = tags_summary.tag_duration.astype(str) + "s"
    # tags_summary = tags_summary.reindex(list(SPECIES_LABELS.keys()))
    # # tags_summary["species"] = tags_summary.index
    # tags_summary.reset_index(inplace=True)
    # tags_summary
    # (ggplot(data=tags_summary,
    #         mapping=aes(x="factor(species, ordered=False)", y="tag_duration", fill="factor(species, ordered=False)"))
    #  + geom_bar(stat="identity", show_legend=False)
    #  + xlab("Species")
    #  + ylab("Duration of annotations (s)")
    #  + geom_text(mapping=aes(label="count"), nudge_y=15)
    #  + theme_classic()
    #  + scale_x_discrete(limits=SPECIES_LIST, labels=xlabels)).save("species_repartition_duration_mini.png", width=10, height=8)

    # (ggplot(data=tags_summary,
    #         mapping=aes(x="factor(species, ordered=False)", y="count", fill="factor(species, ordered=False)"))
    #  + geom_bar(stat="identity", show_legend=False)
    #  + xlab("Species")
    #  + ylab("Number of annotations")
    #  + geom_text(mapping=aes(label="duration"), nudge_y=15)
    #  + theme_classic()
    #  + scale_x_discrete(limits=SPECIES_LIST, labels=xlabels)).save("species_repartition_count_mini.png", width=10, height=8)
    # print(tags_summary)

    # xlabels = [lab.replace(" ", "\n") for lab in SPECIES_LABELS.values()]
    # xlabels
    # plt = (ggplot(data=tags_df, mapping=aes(x='factor(species, ordered=False)', fill="factor(species, ordered=False)"))
    #        # , width=0.4,    position=position_dodge(width=0.5))
    #        + xlab("Species")
    #        + ylab("Number of annotations")
    #        + geom_bar(show_legend=False)
    #        + theme(axis_title=element_text(size=18),
    #                axis_text=element_text(size=10))
    #        # + theme(legend_title="Species")
    #        # + scale_fill_discrete(guide=False, limits=SPECIES_LIST,
    #        #                       labels=list(SPECIES_LABELS.values()))
    #        + scale_x_discrete(limits=SPECIES_LIST, labels=xlabels))
    # print(plt)
    # plt.save("species_repartition_all.png", width=10, height=8)
