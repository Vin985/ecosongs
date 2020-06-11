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

    def load_data(self):
        try:
            if not self.dbmanager:
                raise AttributeError(
                    "No database manager provided. Cannot load data")
            if not self.TABLE_NAME:
                raise AttributeError(
                    "No table name provided. Cannot load data")
            self.df = self.dbmanager.get_table(self.TABLE_NAME)
            return(self._df.loc[:, self._df.columns.intersection(self.columns)])
        except Exception as e:
            print(e)
            self._df = pd.DataFrame()

    @property
    def df(self):
        if self._df is None:
            self.load_data()
        return self._df

    @df.setter
    def df(self, df):
        self._df = self.check_ids(df)

    @property
    def empty(self):
        return self.df.empty

    def check_types(self):
        if self.COLUMNS_TYPE:
            for k, v in self.COLUMNS_TYPE.items():
                print(k)
                print(v)
                self._df[k] = self._df[k].astype(v)
        print(self._df.dtypes)
        print(self._df.memory_usage())

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

    def update_table(self, table, **kwargs):
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
        print(self.df)
        if not columns:
            new = self.df.drop(rows)
        else:
            new = self.remove_rows(self.df, columns, rows)
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
        to_export = table or self.df
        self.dbmanager.export_table(to_export, options["dest"])

    def import_table(self):
        pass
