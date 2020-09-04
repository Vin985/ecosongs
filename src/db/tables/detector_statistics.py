from db.dbmodels import TableDBModel


class DetectorStatisticsTable(TableDBModel):
    TABLE_NAME = "detector_statistics"
    COLUMNS = [
        "analysis_options",
        "n_events",
        "n_tags",
        "true_positive_events",
        "true_positive_tags",
        "false_negative",
        "n_tags_matched",
        "precision",
        "recall",
        "F1_score",
    ]
    DUPLICATE_COLUMNS = ["analysis_options"]

    def __init__(self, df=None, dbmanager=None):
        TableDBModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)
