from config import (
    part_table_names,
    part_parent_table_names
)
from actions.Action import Action
from database.utils import load_tables


class CheckPartCompatability(Action):
    def __init__(self):
        self._name = "CheckPartCompatability"
        self._descripption = "Checks part compatability"

    def perform(self, db, part_ids):
        mb_id = part_ids.get("mb_id")
        cpu_id = part_ids.get("cpu_id")
        ram_id = part_ids.get("ram_id")

        part_tables, parent_tables = load_tables(
            db, part_table_names, part_parent_table_names
        )
        compatability_issues = []
        motherboard = (
            db.session.query(part_tables.get("motherboards"))
            .filter_by(id=mb_id)
            .first()
        )
        processor = (
            db.session.query(part_tables.get("processors")).filter_by(id=cpu_id).first()
        )
        random_access_memory = (
            db.session.query(part_tables.get("random_access_memory"))
            .filter_by(id=ram_id)
            .first()
        )

        if motherboard and processor:
            if motherboard.socket_id != processor.socket_id:
                compatability_issues.append("cpuSocketMismatchMessage")
        if processor and random_access_memory:
            if processor.memory_type_id != random_access_memory.memory_type_id:
                compatability_issues.append("cpuRandomAccessMemoryMismatchMessage")
            if (
                processor.max_memory_supported_gb
                < random_access_memory.total_capacity_gb
            ):
                compatability_issues.append("cpuRandomAccessMemoryCapacityMessage")
        if motherboard and random_access_memory:
            if motherboard.memory_type_id != random_access_memory.memory_type_id:
                compatability_issues.append("mbRandomAccessMemoryMismatchMessage")
            if (
                motherboard.max_memory_supported_gb
                < random_access_memory.total_capacity_gb
            ):
                compatability_issues.append("mbRandomAccessMemoryCapacityMessage")
        if random_access_memory:
            if random_access_memory.modules < 2:
                compatability_issues.append("ramDualChannelWarningMessage")
        return {"compatability_issues": compatability_issues}
