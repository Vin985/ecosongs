import pandas as pd

from audio.recording import Recording
from db.models import TableModel


class AnalysisOptionsTable(TableModel):
    TABLE_NAME = "analysis_options"
    COLUMNS = ["type", "options"]
    DUPLICATE_COLUMNS = ["type", "options"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def add(self, options, type, save=False, replace=True):
        opts = ""
        existing = None
        opt_id = 0

        if type == "event_detection":
            opts = str(options["initargs"][2])
            print("options: " + str(opts))

        if opts and self.df.shape[0] > 0:
            existing = self.df.loc[(self.df["type"] == type) & (
                self.df["options"] == opts)]
            print("existing: " + str(existing))

        if existing.shape[0] > 0:
            opt_id = int(existing.id.iloc[0])
        else:
            opt_id = self.next_id
            new = pd.DataFrame(
                [{"id": self.next_id, "type": type, "options": str(opts)}])
            self.next_id += 1

            if save:
                dest = self.df
                self.update(table=dest.append(new, ignore_index=True, sort=True),
                            save=save)
        print(opt_id)
        return opt_id

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
