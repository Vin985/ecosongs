import pandas as pd

from audio.recording import Recording
from db.dbmodels import TableDBModel


class AnalysisOptionsTable(TableDBModel):
    TABLE_NAME = "analysis_options"
    COLUMNS = ["analysis_type", "options"]
    DUPLICATE_COLUMNS = ["analysis_type", "options"]

    def __init__(self, df=None, dbmanager=None):
        TableDBModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def add(self, options, analysis_type, save=False, replace=True):

        if isinstance(options, list):
            # if analysis_type is None:
            #     raise AttributeError(
            #         "Analysis type should be provided if options is a list")
            opts = self.format_options_list(options)
            new = pd.DataFrame(
                {"analysis_type": [analysis_type] * len(opts), "options": opts}
            )
        elif isinstance(options, dict):
            # if analysis_type is None:
            #     raise AttributeError(
            #         "Analysis type should be provided if options is a dict")
            opts = self.format_options(options)
            new = pd.DataFrame([{"analysis_type": analysis_type, "options": opts}])
        # elif isinstance(options, pd.DataFrame):
        #     pass
        else:
            raise AttributeError(
                "options attribute should be a list of dicts or a dict"
            )

        # existing = None
        # opt_id = 0

        # if opts and self.df.shape[0] > 0:
        #     existing = self.df.loc[(self.df["analysis_type"] == analysis_type) &
        #                            self.df["options"].isin(opts)]
        # print("existing: " + str(existing))

        # if existing is not None and existing.shape[0] > 0:
        #     opt_id = int(existing.id.iloc[0])
        # else:

        res = super().add(new, save, replace)
        # dest = self.df
        # self.update(table=dest.append(new, ignore_index=True, sort=True),
        #             save=save)
        return res

    def format_options_list(self, option_list):
        return [self.format_options(options) for options in option_list]

    def format_options(self, options):
        opts = ";".join([k + ":" + str(v) for k, v in options.items()])
        return opts

    def expand_options(self, dataframe):
        # options are stored in the form "option1:value1;option2:value2"
        # split options to create new dataframe on special characters
        # : or ;
        # This creates a new dataframe where each even column is a column name
        # and every odd column is the associated value
        tmp = dataframe.options.str.split(r";|:", expand=True)
        # get number of columns
        ncols = tmp.shape[1]
        # get first row
        row = tmp.iloc[0]
        # every even colum is actually a column name
        colnames_idx = list(range(0, ncols, 2))
        # Save column names
        colnames = list(row[colnames_idx])
        colnames = [x.strip() for x in colnames]
        # Drop useless columns
        tmp.drop(tmp.columns[colnames_idx], inplace=True, axis=1)
        # Rename columns
        tmp.columns = colnames
        # Concatenate the new dataframe to the old one
        res = pd.concat([dataframe, tmp], axis=1)
        return res
