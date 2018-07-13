# from pony import orm

# db = orm.Database()
# db.bind(provider="sqlite", filename="ecosongs.sqlite", create_db=True)
#
#
# class RecordingModel(db.Entity):
#     _table_ = "Recording"
#     id = orm.PrimaryKey(int, auto=True)
#     name = orm.Required(str, unique=True)
#
#
# orm.sql_debug(True)
# #db.generate_mapping(create_tables=True)


import peewee

db = peewee.SqliteDatabase('db/ecosongs.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class RecordingModel(BaseModel):
    name = peewee.CharField()

    class Meta:
        table_name = 'recordings'


db.connect(reuse_if_open=True)
db.create_tables([RecordingModel], safe=True)
