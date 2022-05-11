from config import part_table_names, vendor_table_name
from actions.Action import Action
from database.utils import load_tables


class DeleteVendor(Action):
    def __init__(self):
        self._name = "DeleteVendor"
        self._descripption = "Deletes vendor from the database"

    def perform(self, db, vendor_id):
        tables, parent_tables = load_tables(db, [vendor_table_name], part_table_names)
        vendor_table = tables.get(vendor_table_name)
        statement = vendor_table.delete().where(vendor_table.c.id==vendor_id)
        db.engine.execute(statement)
