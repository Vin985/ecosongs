import pandas as pd


class BaseModel:
    COLUMNS = []

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

    def __init__(self, columns, df=pd.DataFrame(), dbmanager=None, table=None):
        self._df = df
        # TODO: Change to externalize dbmanager
        if table:
            self.TABLE_NAME = table
        self.dbmanager = dbmanager
        self.columns = columns

    def load_data(self):
        try:
            self._df = self.dbmanager.get_table(self.TABLE_NAME)
            return(self._df.loc[:, self._df.columns.intersection(self.columns)])
            # self._df["date"] = pd.to_datetime(self._df["date"])
        except KeyError:
            self._df

    @property
    def df(self):
        if self._df.empty:
            self.load_data()
        return self._df

    @property
    def empty(self):
        return self._df.empty

    def update(self):
        self.dbmanager.update(self.TABLE_NAME, self._df)

    def create(self):
        self.dbmanager.create(self.TABLE_NAME, self._df)

    def query(self, query):
        return self._df.query(query)

    def append(self, new, save=False):
        # TODO: check duplicates
        # TODO: add idx column?
        # TODO: check duplicates
        self._df = self.df.append(new, ignore_index=True, sort=True)
        if save:
            self.update()
