from db.models import TableModel


class TagsTable(TableModel):
    TABLE_NAME = "tags"
    COLUMNS = [
        "tag_index",
        "recording_id",
        "tag",
        "file_path",
        "tag_start",
        "tag_end",
        "related",
        "overlap",
        "background",
        "tag_duration",
        "noise",
    ]
    COLUMNS_TYPE = {
        "recording_id": int,
    }
    DUPLICATE_COLUMNS = ["recording_id", "tag", "tag_start", "tag_end"]

    NOISE = {"rain": 1, "wind": 2}

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def get_recording_tags(self, recording_id):
        return self.df.loc[self.df.recording_id == recording_id]

    # test if rain or wind:
    # df.loc[(df.noise & NOISE["rain"]) > 0 ]
