from config import part_table_names, \
    build_table_name, \
    build_full_join_map, \
    ignored_build_filter_fields
from actions.Action import Action
from database.pages import get_current_and_total_pages
from database.filters import get_resource_filters
from database.resources import get_resources
from database.utils import load_tables

class GetBuilds(Action):
    def __init__(self):
        self._name = 'GetBuilds'
        self._descripption = 'Returns build data'

    def perform(self, db, offset, filters, by_popularity):
        tables, parent_tables = load_tables(
            db,
            [build_table_name],
            part_table_names
        )
        build_table = tables.get(build_table_name)

        filter_data = get_resource_filters(
            db,
            build_table,
            parent_tables,
            build_full_join_map,
            ignored_build_filter_fields
        )
        current_page, total_pages, offset = get_current_and_total_pages(
            db,
            build_table,
            filters,
            current_page=offset
        )
        builds = get_resources(
            db,
            build_table,
            parent_tables,
            offset,
            filters,
            build_full_join_map,
            by_popularity
        )
        return {
            'filters': filter_data,
            'currentPage': current_page,
            'totalPages': total_pages,
            'builds': builds
        }
