# Initial load
records_per_page = 10
default_page = 1

# Database
db_creds = {
    "name": "pcdb_test",
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": 5432,
}
db_uri = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    db_creds.get("user"),
    db_creds.get("password"),
    db_creds.get("host"),
    db_creds.get("port"),
    db_creds.get("name"),
)

# Table names
build_table_name = "builds"
vendor_table_name = "vendor"
product_table_name = "product"
part_table_names = [
    "processors",
    "graphics_cards",
    "drives",
    "motherboards",
    "random_access_memory",
    "power_supplies",
]
part_parent_table_names = [
    "brands",
    "sockets",
    "ram_memory_types",
    "cpu_series",
    "integrated_graphics",
    "gpu_chipset_manufacturers",
    "gpu_memory_types",
    "interfaces",
    "drive_series",
    "drive_types",
    "drive_form_factors",
    "ram_series",
    "mb_chipsets",
    "mb_form_factors",
    "psu_series",
    "energy_efficiencies",
    "modularity",
]

product_parent_table_names = [
    "vendor",
]

# Join maps
part_full_join_map = {
    "shared": {"brand_id": "brands", "socket_id": "sockets"},
    "processors": {
        "series_id": "cpu_series",
        "integrated_graphics_id": "integrated_graphics",
        "memory_type_id": "ram_memory_types",
    },
    "graphics_cards": {
        "chipset_manufacturer": "gpu_chipset_manufacturers",
        "memory_type_id": "gpu_memory_types",
        "interface_id": "interfaces",
    },
    "drives": {
        "series_id": "drive_series",
        "drive_type_id": "drive_types",
        "form_factor_id": "drive_form_factors",
        "interface_id": "interfaces",
    },
    "random_access_memory": {
        "series_id": "ram_series",
        "memory_type_id": "ram_memory_types",
    },
    "motherboards": {
        "chipset_id": "mb_chipsets",
        "form_factor_id": "mb_form_factors",
        "memory_type_id": "ram_memory_types",
    },
    "power_supplies": {
        "series_id": "psu_series",
        "energy_efficiency_id": "energy_efficiencies",
        "modularity_id": "modularity",
    },
}

vendor_full_join_map = {"shared": {}, vendor_table_name: {}}

product_full_join_map = {
    "shared": {"vendor_id": vendor_table_name},
    product_table_name: {},
}

build_full_join_map = {
    "shared": {
        "processor_id": "processors",
        "graphics_card_id": "graphics_cards",
        "motherboard_id": "motherboards",
        "power_supply_id": "power_supplies",
        "random_access_memory_id": "random_access_memory",
        "drive_id": "drives",
    },
    build_table_name: {},
}

# Fields to not use during filtering
ignored_build_filter_fields = ["id", "popularity"]
ignored_part_filter_fields = ["id", "name", "model", "image_url"]
ignored_vendor_filter_fields = []
ignored_product_filter_fields = []
