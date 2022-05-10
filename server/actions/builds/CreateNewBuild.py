from config import part_table_names, build_table_name
from actions.Action import Action
from database.utils import load_tables


class CreateNewBuild(Action):
    def __init__(self):
        self._name = "CreateNewBuild"
        self._descripption = "Inserts new build into the database"

    def perform(self, db, data):
        data["popularity"] = 1
        tables, parent_tables = load_tables(db, [build_table_name], part_table_names)
        build_table = tables.get(build_table_name)
        statement = build_table.insert().values(**data)
        db.engine.execute(statement)
