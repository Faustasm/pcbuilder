def get_resource_filters(
    db,
    resource_table,
    resource_parent_tables,
    resource_full_join_map,
    ignored_resource_filter_fields,
):
    filters = []
    resource_name = resource_table.name
    shared_parent_table_names = resource_full_join_map.get("shared")
    individual_parent_table_names = resource_full_join_map.get(resource_name)

    for col in resource_table.c:
        filter_name = col.name
        if filter_name not in ignored_resource_filter_fields:
            if filter_name in shared_parent_table_names:
                parent_table_name = shared_parent_table_names.get(filter_name)
                parent_table = resource_parent_tables.get(parent_table_name)
                key = "name" if "name" in parent_table.c else "model"
                q = (
                    db.session.query(parent_table.c.id, parent_table.c[key])
                    .distinct()
                    .join(resource_table, parent_table.c.id == col)
                    .all()
                )
                result = [{"id": r, "name": r1} for (r, r1) in q]
                filters.append({"filter_name": filter_name, "values": result})
            elif filter_name in individual_parent_table_names:
                parent_table_name = individual_parent_table_names.get(filter_name)
                parent_table = resource_parent_tables.get(parent_table_name)
                key = "name" if "name" in parent_table.c else "model"
                q = (
                    db.session.query(parent_table.c.id, parent_table.c[key])
                    .distinct()
                    .join(resource_table, parent_table.c.id == col)
                    .all()
                )
                result = [{"id": r, "name": r1} for (r, r1) in q]
                filters.append({"filter_name": filter_name, "values": result})
            else:
                q = db.session.query(col).distinct().all()
                result = [{"id": r, "name": r} for (r,) in q]
                filters.append({"filter_name": filter_name, "values": result})
    return filters
