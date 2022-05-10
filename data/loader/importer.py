from pypika import Query, Table

class Importer:
    def __init__(self, postgre_sql_client):
        self.postgre_sql_client = postgre_sql_client

    def import_record(self, table_name, row_dict):
        table =  Table(table_name)
        return self.postgre_sql_client.insert(
            str(
                table.insert(
                    *[
                        row_dict.get(key) if row_dict.get(key) else None for key in row_dict
                    ]
                )
            )
        )
