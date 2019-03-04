from db.models import TableModel


class SongEventsTable(TableModel):
    TABLE_NAME = "song_events"
    COLUMNS = ["event_id", "recording_id", "start", "end"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def add(self, new, save=False, replace=True):
        # TODO: check duplicates
        # TODO: add idx column?
        # TODO: check duplicates
        print(self.df)
        new = self.check_ids(new)
        if replace:
            to_remove = new["recording_id"].unique()
            self.df = self.df.loc[~self.df.recording_id.isin(to_remove)]
        self.df = self.df.append(new, ignore_index=True, sort=True)
        self.save(update=True)

    def get_events(self, recording_id):
        return self.df[self.df["recording_id"] == recording_id]
