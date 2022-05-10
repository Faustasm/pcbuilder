from config import (
    product_parent_table_names,
    product_table_name,
    product_full_join_map,
    ignored_product_filter_fields,
)
from actions.Action import Action
from database.pages import get_current_and_total_pages
from database.filters import get_resource_filters
from database.resources import get_resources
from database.utils import load_tables


class GetProducts(Action):
    def __init__(self):
        self._name = "GetProducts"
        self._descripption = "Returns product data"

    def perform(self, db, offset, filters):
        tables, parent_tables = load_tables(
            db, [product_table_name], product_parent_table_names
        )
        product_table = tables.get(product_table_name)

        filter_data = get_resource_filters(
            db,
            product_table,
            parent_tables,
            product_full_join_map,
            ignored_product_filter_fields,
        )
        current_page, total_pages, offset = get_current_and_total_pages(
            db, product_table, filters, current_page=offset
        )
        products = get_resources(
            db,
            product_table,
            parent_tables,
            offset,
            filters,
            product_full_join_map,
            False,
        )
        return {
            "filters": filter_data,
            "currentPage": current_page,
            "totalPages": total_pages,
            "products": products,
        }
