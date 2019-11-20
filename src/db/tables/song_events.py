from db.models import TableModel


class SongEventsTable(TableModel):
    TABLE_NAME = "song_events"
    COLUMNS = ["event_id", "recording_id", "start", "end", "analysis_options"]
    DUPLICATE_COLUMNS = ["recording_id", "analysis_options"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def get_duplicates_dict(self, df):
        recs = df["recording_id"].unique()
        analysis = df["analysis_options"].unique()
        return {"recording_id": recs, "analysis_options": analysis}

    # def add(self, new, save=False, replace=True):
    #     # TODO: check duplicates
    #     # TODO: add idx column?
    #     # TODO: check duplicates
    #     print(self.df)
    #     new = self.check_ids(new)
    #     if replace:
    #         to_remove = new["recording_id"].unique()
    #         self.df = self.df.loc[~self.df.recording_id.isin(to_remove)]
    #     self.update(self.df.append(new, ignore_index=True, sort=True), save=save)

    def get_events(self, recording_id, analysis_options=[]):
        return self.df[self.df["recording_id"] == recording_id]
