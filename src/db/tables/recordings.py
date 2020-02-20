from audio.recording import Recording
from db.models import TableModel


class RecordingsTable(TableModel):
    TABLE_NAME = "recordings"
    COLUMNS = ["name", "year", "site",
               "plot", "date", "path",
               "ext", "recorder", "duration", "sample_rate"]  # , "old_name"]
    DUPLICATE_COLUMNS = ["name", "plot", "site", "year"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS,
                            df=df, dbmanager=dbmanager)
        self.recordings = {}

    def load_recordings(self, indexes):
        """Create Recording objects from indexes if they had not been loaded
        in memory before.

        Parameters
        ----------
        indexes : type
            Description of parameter `indexes`.

        Returns
        -------
        type
            Description of returned object.

        """
        to_load = [idx for idx in indexes if idx not in self.recordings]
        if to_load:
            to_load = self._df.loc[indexes]
            to_update = {row.id: Recording(row._asdict())
                         for row in to_load.itertuples(index=True)}
            self.recordings.update(to_update)
        return [self.recordings[idx] for idx in indexes]

    def get_recording(self, idx):
        if idx in self.recordings.keys():
            rec = self.recordings[idx]
        else:
            rec = Recording(self._df.loc[idx].to_dict())
            self.recordings[idx] = rec
        return rec
