from config import part_table_names, product_table_name
from actions.Action import Action
from database.utils import load_tables
from bcrypt import checkpw, hashpw, gensalt


class CreateNewProduct(Action):
    def __init__(self):
        self._name = "CreateNewProduct"
        self._descripption = "Inserts new product into the database"

    def perform(self, db, data):
        tables, parent_tables = load_tables(db, [product_table_name], part_table_names)
        product_table = tables.get(product_table_name)
        vendor_id = data.get("vendor_id")
        vendor = db.session.query(product_table).filter_by(id=vendor_id).first()
        key_bytes = bytes(data.pop("key"), "utf-8")
        authentication_success = checkpw(key_bytes, vendor.key.encode("utf-8"))
        if authentication_success:
            statement = product_table.insert().values(**data)
            db.engine.execute(statement)
            return {"message": "Product created"}
        return {"error": "auth_failed"}
