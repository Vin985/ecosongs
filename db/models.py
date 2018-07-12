from pony import orm

db = orm.Database("sqlite", "db/ecosongs.sqlite", create_db=True)


class RecordingModel(orm.db.Entity):
    table = "_Recording_"
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str, unique=True)


db.generate_mapping(create_tables=True)
