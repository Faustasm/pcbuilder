def load_tables(db, resource_table_names, resource_parent_table_names):
    resource_tables = {}
    parent_tables = {}

    for table_name in resource_table_names:
        resource_tables[table_name] = db.Table(
            table_name, db.metadata, autoload=True, autoload_with=db.engine
        )

    for table_name in resource_parent_table_names:
        parent_tables[table_name] = db.Table(
            table_name, db.metadata, autoload=True, autoload_with=db.engine
        )

    return resource_tables, parent_tables
