from config import records_per_page


def get_resources(
        db,
        resource_table,
        parent_tables,
        offset,
        filters,
        resource_full_join_map,
        order_by_popularity=False
    ):
    resources = []
    resource_name = resource_table.name
    resources_to_query = [resource_table]
    join_params = []
    column_names = [col.name for col in resource_table.c]

    shared_parent_table_names = resource_full_join_map.get('shared')
    individual_parent_table_names = resource_full_join_map.get(
        resource_name
    )

    for col in resource_table.c:
        column_name = col.name
        parent_table_name = shared_parent_table_names.get(column_name) \
            if column_name in resource_full_join_map.get('shared') \
            else individual_parent_table_names.get(column_name)

        if parent_table_name:
            parent_table = parent_tables.get(parent_table_name)
            column_names.append(parent_table.name)
            key = 'name' if 'name' in parent_table.c else 'model'
            resources_to_query.append(
                parent_table.c[key]
            )

            join_params.append((parent_table, parent_table.c.id==col))

    session = db.session
    q = session.query(*resources_to_query).filter_by(
        **filters
    )
    if join_params:
        q = q.outerjoin(*join_params)
    if order_by_popularity:
        builds_table = resources_to_query[0]
        q = q.order_by(builds_table.c.popularity.desc())

    q = q.offset(offset).limit(records_per_page)
    q.all()

    for item in q:
        part_dict = {}
        for i in range(len(column_names)):
            part_dict[column_names[i]] = item[i]
        resources.append(part_dict)
    return resources
