from config import (
    part_table_names,
    vendor_table_name,
    vendor_full_join_map,
    ignored_vendor_filter_fields,
)
from actions.Action import Action
from database.pages import get_current_and_total_pages
from database.filters import get_resource_filters
from database.resources import get_resources
from database.utils import load_tables


class GetVendors(Action):
    def __init__(self):
        self._name = "GetVendors"
        self._descripption = "Returns vendor data"

    def perform(self, db, offset, filters):
        tables, parent_tables = load_tables(db, [vendor_table_name], part_table_names)
        vendor_table = tables.get(vendor_table_name)

        filter_data = get_resource_filters(
            db,
            vendor_table,
            parent_tables,
            vendor_full_join_map,
            ignored_vendor_filter_fields,
        )
        current_page, total_pages, offset = get_current_and_total_pages(
            db, vendor_table, filters, current_page=offset
        )
        vendors = get_resources(
            db,
            vendor_table,
            parent_tables,
            offset,
            filters,
            vendor_full_join_map,
            False,
        )
        return {
            "filters": filter_data,
            "currentPage": current_page,
            "totalPages": total_pages,
            "vendors": vendors,
        }
