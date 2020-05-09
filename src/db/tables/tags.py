from db.models import TableModel


class TagsTable(TableModel):
    TABLE_NAME = "tags"
    COLUMNS = ["recording_id", "tag", "file_path", "tag_start",
               "tag_end", "related", "overlap", "background"]
    DUPLICATE_COLUMNS = ["recording_id", "tag", "tag_start", "tag_end"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)
