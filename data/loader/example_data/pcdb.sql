CREATE TABLE "brands" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "cpu_series" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "integrated_graphics" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "processors" (
  "id" SERIAL PRIMARY KEY,
  "brand_id" int NOT NULL,
  "name" varchar NOT NULL,
  "series_id" int NOT NULL,
  "socket_id" int NOT NULL,
  "number_of_cores" int NOT NULL,
  "number_of_threads" int NOT NULL,
  "memory_type_id" int NOT NULL,
  "max_memory_supported" int NOT NULL,
  "max_memory_speed" int NOT NULL,
  "operating_frequency_mhz" float NOT NULL,
  "turbo_frequency_mhz" float NOT NULL,
  "thermal_design_power_w" int NOT NULL,
  "cooling_device_included" bool NOT NULL,
  "integrated_graphics_id" int,
  "image_url" varchar NOT NULL
);

CREATE TABLE "drive_series" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "drive_types" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "drive_form_factors" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "drives" (
  "id" SERIAL PRIMARY KEY,
  "brand_id" int NOT NULL,
  "series_id" int NOT NULL,
  "drive_type_id" int NOT NULL,
  "form_factor_id" int NOT NULL,
  "model" varchar NOT NULL,
  "capacity_gb" int NOT NULL,
  "max_read_mb_s" int NOT NULL,
  "max_write_mb_s" int NOT NULL,
  "interface_id" int NOT NULL,
  "image_url" varchar NOT NULL
);

CREATE TABLE "gpu_chipset_manufacturers" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "gpu_memory_types" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "gpu_outputs" (
  "id" SERIAL PRIMARY KEY,
  "graphics_card_id" int NOT NULL,
  "output_id" int NOT NULL,
  "quantity" int NOT NULL
);

CREATE TABLE "gpu_power_connectors" (
  "id" SERIAL PRIMARY KEY,
  "graphics_card_id" int NOT NULL,
  "power_connector_id" int NOT NULL,
  "quantity" int NOT NULL
);

CREATE TABLE "graphics_cards" (
  "id" SERIAL PRIMARY KEY,
  "brand_id" int NOT NULL,
  "name" varchar NOT NULL,
  "model" varchar NOT NULL,
  "chipset_manufacturer_id" int NOT NULL,
  "memory_type_id" int NOT NULL,
  "memory_size_gb" int NOT NULL,
  "thermal_design_power_w" int NOT NULL,
  "slot_width" int NOT NULL,
  "interface_id" int NOT NULL,
  "image_url" varchar NOT NULL
);

CREATE TABLE "mb_chipset_manufacturers" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "mb_chipsets" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "manufacturer_id" int NOT NULL
);

CREATE TABLE "mb_form_factors" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "mb_interfaces" (
  "id" SERIAL PRIMARY KEY,
  "motherboard_id" int NOT NULL,
  "interface_id" int NOT NULL,
  "quantity" int NOT NULL,
  "type" varchar NOT NULL
);

CREATE TABLE "mb_outputs" (
  "id" SERIAL PRIMARY KEY,
  "motherboard_id" int NOT NULL,
  "output_id" int NOT NULL,
  "quantity" int NOT NULL
);

CREATE TABLE "motherboards" (
  "id" SERIAL PRIMARY KEY,
  "brand_id" int NOT NULL,
  "model" varchar NOT NULL,
  "socket_id" int NOT NULL,
  "chipset_id" int NOT NULL,
  "form_factor_id" int NOT NULL,
  "memory_type_id" int NOT NULL,
  "max_memory_supported" int NOT NULL,
  "memory_slots" int NOT NULL,
  "image_url" varchar NOT NULL
);

CREATE TABLE "adapters" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "power_connector_connection_configurations" (
  "id" SERIAL PRIMARY KEY,
  "power_connector_id" int NOT NULL,
  "connection_configuration_id" int NOT NULL
);

CREATE TABLE "connection_configurations" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "energy_efficiencies" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "modularity" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "power_connectors" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "psu_series" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "psu_adapters" (
  "id" SERIAL PRIMARY KEY,
  "power_supply_id" int NOT NULL,
  "adapter_id" int NOT NULL,
  "quantity" int NOT NULL
);

CREATE TABLE "psu_power_connectors" (
  "id" SERIAL PRIMARY KEY,
  "power_supply_id" int NOT NULL,
  "power_connector_id" int NOT NULL,
  "cable_count" int NOT NULL,
  "connector_count" int NOT NULL
);

CREATE TABLE "power_supplies" (
  "id" SERIAL PRIMARY KEY,
  "brand_id" int NOT NULL,
  "series_id" int NOT NULL,
  "model" varchar NOT NULL,
  "max_power_w" int NOT NULL,
  "energy_efficiency_id" int NOT NULL,
  "modularity_id" int NOT NULL,
  "image_url" varchar NOT NULL
);

CREATE TABLE "ram_memory_types" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "ram_series" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "random_access_memory" (
  "id" SERIAL PRIMARY KEY,
  "brand_id" int NOT NULL,
  "series_id" int NOT NULL,
  "model" varchar NOT NULL,
  "memory_type_id" int NOT NULL,
  "timing" varchar NOT NULL,
  "cas_latency" int NOT NULL,
  "voltage" float NOT NULL,
  "transfer_rate_mb" int NOT NULL,
  "speed" int NOT NULL,
  "modules" int NOT NULL,
  "module_capacity_gb" int NOT NULL,
  "total_capacity_gb" int NOT NULL,
  "image_url" varchar NOT NULL
);

CREATE TABLE "interfaces" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "version" float
);

CREATE TABLE "outputs" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "sockets" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "vendor" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "product" (
  "id" SERIAL PRIMARY KEY,
  "vendor_id" int NOT NULL,
  "product_id" int NOT NULL,
  "type" varchar NOT NULL,
  "price" money NOT NULL
);

CREATE TABLE "builds" (
  "id" SERIAL PRIMARY KEY,
  "processor_id" int NOT NULL,
  "graphics_card_id" int NOT NULL,
  "motherboard_id" int NOT NULL,
  "power_supply_id" int NOT NULL,
  "random_access_memory_id" int NOT NULL,
  "drive_id" int NOT NULL,
  "popularity" int NOT NULL
);

ALTER TABLE "processors" ADD FOREIGN KEY ("id") REFERENCES "builds" ("processor_id");

ALTER TABLE "graphics_cards" ADD FOREIGN KEY ("id") REFERENCES "builds" ("graphics_card_id");

ALTER TABLE "motherboards" ADD FOREIGN KEY ("id") REFERENCES "builds" ("motherboard_id");

ALTER TABLE "power_supplies" ADD FOREIGN KEY ("id") REFERENCES "builds" ("power_supply_id");

ALTER TABLE "random_access_memory" ADD FOREIGN KEY ("id") REFERENCES "builds" ("random_access_memory_id");

ALTER TABLE "drives" ADD FOREIGN KEY ("id") REFERENCES "builds" ("drive_id");

ALTER TABLE "cpu_series" ADD FOREIGN KEY ("id") REFERENCES "processors" ("series_id");

ALTER TABLE "integrated_graphics" ADD FOREIGN KEY ("id") REFERENCES "processors" ("integrated_graphics_id");

ALTER TABLE "drive_series" ADD FOREIGN KEY ("id") REFERENCES "drives" ("series_id");

ALTER TABLE "drive_types" ADD FOREIGN KEY ("id") REFERENCES "drives" ("drive_type_id");

ALTER TABLE "drive_form_factors" ADD FOREIGN KEY ("id") REFERENCES "drives" ("form_factor_id");

ALTER TABLE "gpu_chipset_manufacturers" ADD FOREIGN KEY ("id") REFERENCES "graphics_cards" ("chipset_manufacturer_id");

ALTER TABLE "gpu_memory_types" ADD FOREIGN KEY ("id") REFERENCES "graphics_cards" ("memory_type_id");

ALTER TABLE "mb_chipset_manufacturers" ADD FOREIGN KEY ("id") REFERENCES "mb_chipsets" ("manufacturer_id");

ALTER TABLE "mb_chipsets" ADD FOREIGN KEY ("id") REFERENCES "motherboards" ("chipset_id");

ALTER TABLE "mb_form_factors" ADD FOREIGN KEY ("id") REFERENCES "motherboards" ("form_factor_id");

ALTER TABLE "energy_efficiencies" ADD FOREIGN KEY ("id") REFERENCES "power_supplies" ("energy_efficiency_id");

ALTER TABLE "modularity" ADD FOREIGN KEY ("id") REFERENCES "power_supplies" ("modularity_id");

ALTER TABLE "psu_series" ADD FOREIGN KEY ("id") REFERENCES "power_supplies" ("series_id");

ALTER TABLE "ram_memory_types" ADD FOREIGN KEY ("id") REFERENCES "random_access_memory" ("memory_type_id");

ALTER TABLE "ram_memory_types" ADD FOREIGN KEY ("id") REFERENCES "processors" ("memory_type_id");

ALTER TABLE "ram_memory_types" ADD FOREIGN KEY ("id") REFERENCES "motherboards" ("memory_type_id");

ALTER TABLE "ram_series" ADD FOREIGN KEY ("id") REFERENCES "random_access_memory" ("series_id");

ALTER TABLE "adapters" ADD FOREIGN KEY ("id") REFERENCES "psu_adapters" ("adapter_id");

ALTER TABLE "brands" ADD FOREIGN KEY ("id") REFERENCES "processors" ("brand_id");

ALTER TABLE "brands" ADD FOREIGN KEY ("id") REFERENCES "drives" ("brand_id");

ALTER TABLE "brands" ADD FOREIGN KEY ("id") REFERENCES "graphics_cards" ("brand_id");

ALTER TABLE "brands" ADD FOREIGN KEY ("id") REFERENCES "motherboards" ("brand_id");

ALTER TABLE "brands" ADD FOREIGN KEY ("id") REFERENCES "power_supplies" ("brand_id");

ALTER TABLE "brands" ADD FOREIGN KEY ("id") REFERENCES "random_access_memory" ("brand_id");

ALTER TABLE "interfaces" ADD FOREIGN KEY ("id") REFERENCES "graphics_cards" ("interface_id");

ALTER TABLE "interfaces" ADD FOREIGN KEY ("id") REFERENCES "mb_interfaces" ("interface_id");

ALTER TABLE "interfaces" ADD FOREIGN KEY ("id") REFERENCES "drives" ("interface_id");

ALTER TABLE "outputs" ADD FOREIGN KEY ("id") REFERENCES "gpu_outputs" ("output_id");

ALTER TABLE "outputs" ADD FOREIGN KEY ("id") REFERENCES "mb_outputs" ("output_id");

ALTER TABLE "power_connectors" ADD FOREIGN KEY ("id") REFERENCES "gpu_power_connectors" ("power_connector_id");

ALTER TABLE "power_connectors" ADD FOREIGN KEY ("id") REFERENCES "power_connector_connection_configurations" ("power_connector_id");

ALTER TABLE "power_connectors" ADD FOREIGN KEY ("id") REFERENCES "psu_power_connectors" ("power_connector_id");

ALTER TABLE "sockets" ADD FOREIGN KEY ("id") REFERENCES "processors" ("socket_id");

ALTER TABLE "sockets" ADD FOREIGN KEY ("id") REFERENCES "motherboards" ("socket_id");

ALTER TABLE "graphics_cards" ADD FOREIGN KEY ("id") REFERENCES "gpu_outputs" ("graphics_card_id");

ALTER TABLE "graphics_cards" ADD FOREIGN KEY ("id") REFERENCES "gpu_power_connectors" ("graphics_card_id");

ALTER TABLE "motherboards" ADD FOREIGN KEY ("id") REFERENCES "mb_interfaces" ("motherboard_id");

ALTER TABLE "motherboards" ADD FOREIGN KEY ("id") REFERENCES "mb_outputs" ("motherboard_id");

ALTER TABLE "connection_configurations" ADD FOREIGN KEY ("id") REFERENCES "power_connector_connection_configurations" ("connection_configuration_id");

ALTER TABLE "power_supplies" ADD FOREIGN KEY ("id") REFERENCES "psu_power_connectors" ("power_supply_id");

ALTER TABLE "power_supplies" ADD FOREIGN KEY ("id") REFERENCES "psu_adapters" ("power_supply_id");

ALTER TABLE "vendor" ADD FOREIGN KEY ("id") REFERENCES "product" ("vendor_id");
