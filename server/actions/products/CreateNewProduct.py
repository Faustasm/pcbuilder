from config import part_table_names, product_table_name
from actions.Action import Action
from database.utils import load_tables


class CreateNewProduct(Action):
    def __init__(self):
        self._name = "CreateNewProduct"
        self._descripption = "Inserts new product into the database"

    def perform(self, db, data):
        tables, parent_tables = load_tables(db, [product_table_name], part_table_names)
        product_table = tables.get(product_table_name)
        statement = product_table.insert().values(**data)
        db.engine.execute(statement)
