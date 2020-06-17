import pandas as pd


class BaseModel:
    COLUMNS = []
    id = None

    def __init__(self, from_collection):
        if from_collection:
            if type(from_collection) is list:
                if len(from_collection) == len(self.COLUMNS):
                    from_collection = dict(zip(self.COLUMNS, from_collection))
                else:
                    message = ("The provided list has an unexpected length. "
                               "{0} elements found when {1} were expected. "
                               "The {2!s} class expects "
                               "the following elements {3!s}".format(len(from_collection),
                                                                     len(self.COLUMNS),
                                                                     self.__class__,
                                                                     self.COLUMNS))
                    raise ValueError(message)
            self.attrs_from_collection(from_collection)

    def attrs_from_collection(self, collection):
        if collection:
            for key in collection:
                setattr(self, key, collection[key])

    def to_dict(self):
        return {key: getattr(self, key) for key in self.COLUMNS}


class TableModel():
    TABLE_NAME = ""
    COMMON_COLUMNS = ["id"]
    DUPLICATE_COLUMNS = []
    COLUMNS_TYPE = {}
    REFERS_TO = {}
    REFERRED_BY = []

    def __init__(self, columns, df=None, dbmanager=None, table=None):
        # TODO: Change to externalize dbmanager
        if table:
            self.TABLE_NAME = table
        self.dbmanager = dbmanager
        self.columns = self.COMMON_COLUMNS + columns
        self.next_id = 0
        self._df = df

    def __str__(self):
        return str(self.df)

    @property
    def df(self):
        if self._df is None:
            self.load_data()
        return self._df

    @df.setter
    def df(self, df):
        self._df = self.check_columns(df)

    @property
    def empty(self):
        return self.df.empty

    def load_data(self):
        self.df = self.get_table(table=self.TABLE_NAME)

    def get_table(self, **kwargs):
        df = pd.DataFrame()
        if not self.dbmanager:
            raise AttributeError(
                "No database manager provided. Cannot load data")
        if not self.TABLE_NAME:
            raise AttributeError(
                "No table name provided. Cannot load data")
        df = self.dbmanager.get_table(**kwargs)
        return df

    def save(self, update=False):
        self.check_types()
        if update:
            self.dbmanager.update(self.TABLE_NAME, self._df)
        else:
            self.dbmanager.save(self.TABLE_NAME, self._df)

    def update(self, table, save=False, **kwargs):
        self.update_table(table, **kwargs)
        if save:
            self.save(update=True)

    def create(self, table, save=False):
        self._df = table
        if save:
            self.save()

    def update_table(self, table):
        self.df = table

    def query(self, query):
        return self.df.query(query)

    def check_duplicates(self, new, replace=True):
        pass

    def check_ids(self, table):
        if "id" not in table.columns:
            table.loc[:, "id"] = list(
                range(self.next_id, self.next_id + table.shape[0]))
        if not table.empty:
            self.next_id = max(table["id"]) + 1
        return table

    def check_types(self, df=None):
        if self.COLUMNS_TYPE:
            if df is None:
                df = self._df
            for k, v in self.COLUMNS_TYPE.items():
                # TODO: do only if type is different
                df[k] = df[k].astype(v)

    def check_columns(self, df):
        df = self.check_ids(df)
        if not all(item in df.columns for item in self.columns):
            raise ValueError(
                "Not all required columns are present in the loaded table. Please make sure the" +
                " loaded table is the correct one. Required columns are {0}. Only found {1}."
                .format(self.columns, df.columns))
        self.check_types(df)
        return df

    def get_duplicates_dict(self, df):
        return df[self.DUPLICATE_COLUMNS].to_dict(orient='list')

    def remove_duplicates(self, remove_in, remove_from):
        # print("removing duplicates")
        if remove_from.empty:
            return remove_in
        if remove_in.empty:
            return remove_from
        duplicates_dict = self.get_duplicates_dict(remove_from)
        # res = remove_in[~remove_in[self.DUPLICATE_COLUMNS].isin(
        #     duplicates_dict).all(axis=1)]
        res = self.remove_rows(
            remove_in, self.DUPLICATE_COLUMNS, duplicates_dict)
        return res.copy()

    def remove_rows(self, data, columns, dict_values):
        return data.loc[~data[columns].isin(dict_values).all(axis=1)]

    def delete(self, rows, columns=None, save=False):
        if not columns:
            new = self.df.drop(rows)
        else:
            new = self.remove_rows(self.df, columns, rows)
        if new.shape[0] != self.df.shape[0]:
            self.update(table=new, save=save)
            print(self.df)

    def add(self, new, save=False, replace=True):
        dest = self.df
        if replace:
            # if we replace, remove duplicates from old dataframe
            dest = self.remove_duplicates(self.df, new)
        else:
            # remove duplicates from new dataframe
            new = self.remove_duplicates(new, self.df)
        new = self.check_ids(new)
        if not new.empty:
            self.update(table=dest.append(new, ignore_index=True, sort=True),
                        save=save)
        return new

    def get_rows_by_column(self, column, values):
        rows = self.df.loc[self.df[column].isin(values)]
        rows.reset_index(inplace=True, drop=True)
        return rows

    def export_table(self, options, table=None):
        to_export = table if table is not None else self.df
        self.dbmanager.export_table(to_export, options["dest"])
