from config import part_table_names, product_table_name
from actions.Action import Action
from database.utils import load_tables


class UpdateProduct(Action):
    def __init__(self):
        self._name = "UpdateProduct"
        self._descripption = "Updates product in the database"

    def perform(self, db, data, product_id):
        tables, parent_tables = load_tables(db, [product_table_name], part_table_names)
        product_table = tables.get(product_table_name)
        statement = (
            product_table.update()
            .where(product_table.c.id == product_id)
            .values(**data)
        )
        db.engine.execute(statement)
