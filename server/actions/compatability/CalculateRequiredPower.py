from config import (
    part_table_names,
    part_parent_table_names,
    part_full_join_map,
    ignored_part_filter_fields,
)
from actions.Action import Action
from database.pages import get_current_and_total_pages
from database.filters import get_resource_filters
from database.resources import get_resources
from database.utils import load_tables


class CalculateRequiredPower(Action):
    def __init__(self):
        self._name = "CalculateRequiredPower"
        self._descripption = "Calculates required power for build"

    def perform(self, db, part_ids):
        mb_id = part_ids.get("mb_id")
        cpu_id = part_ids.get("cpu_id")
        drive_id = part_ids.get("drive_id")
        ram_id = part_ids.get("ram_id")
        gpu_id = part_ids.get("gpu_id")

        part_tables, parent_tables = load_tables(
            db, part_table_names, part_parent_table_names
        )
        required_power = 0
        motherboard = (
            db.session.query(part_tables.get("motherboards"))
            .filter_by(id=mb_id)
            .first()
        )
        processor = (
            db.session.query(part_tables.get("processors")).filter_by(id=cpu_id).first()
        )
        drive = (
            db.session.query(part_tables.get("drives")).filter_by(id=drive_id).first()
        )
        random_access_memory = (
            db.session.query(part_tables.get("random_access_memory"))
            .filter_by(id=ram_id)
            .first()
        )
        graphics_card = (
            db.session.query(part_tables.get("graphics_cards"))
            .filter_by(id=gpu_id)
            .first()
        )

        if motherboard:
            required_power += 150
        if processor:
            required_power += int(processor.thermal_design_power_w)
        if drive:
            required_power += 30
        if random_access_memory:
            required_power += int(random_access_memory.modules) * 15
        if graphics_card:
            required_power += int(graphics_card.thermal_design_power_w)

        return {"required_power": required_power}
