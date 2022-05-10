from config import records_per_page, default_page


def get_current_and_total_pages(db, resource_table, filters, current_page=None):
    current_page = int(current_page) if current_page else default_page
    offset = int(current_page) * records_per_page
    total_records = len(db.session.query(resource_table).filter_by(**filters).all())

    total_pages = (
        int(total_records / records_per_page)
        if total_records % records_per_page == 0
        else int(total_records / records_per_page) + 1
    )

    if total_pages == 1:
        offset = None

    if offset and offset >= total_records:
        offset = None
    return current_page, total_pages, offset
