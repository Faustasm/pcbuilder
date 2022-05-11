from config import part_table_names, vendor_table_name
from actions.Action import Action
from database.utils import load_tables


class UpdateVendor(Action):
    def __init__(self):
        self._name = "UpdateVendor"
        self._descripption = "Updates vendor in the database"

    def perform(self, db, data, vendor_id):
        tables, parent_tables = load_tables(db, [vendor_table_name], part_table_names)
        vendor_table = tables.get(vendor_table_name)
        statement = (
            vendor_table.update().where(vendor_table.c.id == vendor_id).values(**data)
        )
        db.engine.execute(statement)
