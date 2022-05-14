from config import part_table_names, vendor_table_name
from actions.Action import Action
from database.utils import load_tables
from bcrypt import hashpw, gensalt


class CreateNewVendor(Action):
    def __init__(self):
        self._name = "CreateNewVendor"
        self._descripption = "Inserts new vendor into the database"

    def perform(self, db, data):
        key_bytes = bytes(data.get("key"), "utf-8")
        hashed_key = hashpw(key_bytes, gensalt(10)).decode("utf-8")
        data["key"] = hashed_key
        tables, parent_tables = load_tables(db, [vendor_table_name], part_table_names)
        vendor_table = tables.get(vendor_table_name)
        statement = vendor_table.insert().values(**data)
        db.engine.execute(statement)
