import pandas as pd

from audio.recording import Recording
from db.models import TableModel


class AnalysisOptionsTable(TableModel):
    TABLE_NAME = "analysis_options"
    COLUMNS = ["analysis_type", "options"]
    DUPLICATE_COLUMNS = ["analysis_type", "options"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def add(self, options, analysis_type, save=False, replace=True):
        opts = self.format_options(options)
        existing = None
        opt_id = 0

        if opts and self.df.shape[0] > 0:
            existing = self.df.loc[(self.df["analysis_type"] == analysis_type) & (
                self.df["options"] == opts)]
            # print("existing: " + str(existing))

        if existing is not None and existing.shape[0] > 0:
            opt_id = int(existing.id.iloc[0])
        else:
            opt_id = self.next_id
            new = pd.DataFrame(
                [{"id": self.next_id, "analysis_type": analysis_type, "options": str(opts)}])
            self.next_id += 1
            dest = self.df
            self.update(table=dest.append(new, ignore_index=True, sort=True),
                        save=save)
        return opt_id

    def format_options(self, options):
        opts = "; ".join([k + ":" + str(v) for k, v in options.items()])
        return opts

        # new = self.check_ids(new)
        # if replace:
        #     # if we replace, remove duplicates from old dataframe
        #     dest = self.remove_duplicates(self.df, new)
        # else:
        #     # remove duplicates from new dataframe
        #     dest = self.df
        #     new = self.remove_duplicates(new, self.df)
        # if not new.empty:
        #     self.update(table=dest.append(new, ignore_index=True, sort=True),
        #                 save=save)
