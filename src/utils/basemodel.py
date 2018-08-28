

class BaseModel:
    COLUMNS = []

    def __init__(self, from_collection):
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
        for key in from_collection:
            setattr(self, key, from_collection[key])
