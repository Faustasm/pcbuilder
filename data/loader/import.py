import csv
from glob import glob
from client import PostgreSqlClient
from importer import Importer
from config import *

postgre_sql_client = PostgreSqlClient(
    USER, PASS, HOST, PORT, DB_NAME
)

postgre_sql_client.connect()
importer = Importer(postgre_sql_client)

files_to_import = glob("{}/**/*.csv".format(CSV_DIR), recursive=True)

for file_to_import in files_to_import:
    if file_to_import not in IGNORED_FILES:
        row_dicts = []
        table_name = file_to_import.split("/")[-1].replace(".csv", "")

        with open(file_to_import, "r") as csvFile:
            for row_dict in csv.DictReader(csvFile):
                row_dicts.append(row_dict)
        csvFile.close()

        for row_dict in row_dicts:
            importer.import_record(table_name, row_dict)
