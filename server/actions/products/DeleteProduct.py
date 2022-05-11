from config import part_table_names, product_table_name
from actions.Action import Action
from database.utils import load_tables


class DeleteProduct(Action):
    def __init__(self):
        self._name = "DeleteProduct"
        self._descripption = "Deletes product from the database"

    def perform(self, db, product_id):
        tables, parent_tables = load_tables(db, [product_table_name], part_table_names)
        product_table = tables.get(product_table_name)
        statement = product_table.delete().where(product_table.c.id == product_id)
        db.engine.execute(statement)
