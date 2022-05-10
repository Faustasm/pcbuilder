from config import part_table_names, \
    part_parent_table_names, \
    part_full_join_map, \
    ignored_part_filter_fields
from actions.Action import Action
from database.pages import get_current_and_total_pages
from database.filters import get_resource_filters
from database.resources import get_resources
from database.utils import load_tables


class GetParts(Action):
    def __init__(self):
        self._name = 'GetParts'
        self._descripption = 'Returns part data'

    def perform(self, db, offset, filters, part_name):
        part_tables, parent_tables = load_tables(
            db,
            part_table_names,
            part_parent_table_names
        )
        part_table = part_tables.get(part_name)

        filter_data = get_resource_filters(
            db,
            part_table,
            parent_tables,
            part_full_join_map,
            ignored_part_filter_fields
        )
        current_page, total_pages, offset = get_current_and_total_pages(
            db,
            part_table,
            filters,
            current_page=offset
        )
        parts = get_resources(
            db,
            part_table,
            parent_tables,
            offset,
            filters,
            part_full_join_map,
            False
        )
        return {
            'selectedPart': {
                'endpoint': part_name
            },
            'partsList': part_table_names,
            'filters': filter_data,
            'currentPage': current_page,
            'totalPages': total_pages,
            'parts': parts
        }
