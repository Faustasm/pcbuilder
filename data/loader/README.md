## Script to load csv data to a postgres database from a directory recursively.

### Dependencies
1. Python3
2. python-pip
3. python-virtualenv

### Requirements
1. Csv file name should be the same as the name of the table.
2. Csv columns must be ordered exactly the same as table columns.

### Full usage example

1. Create an ENV in the root directory (same one the README is in) and activate it.
```
python -m venv ENV
source ENV/bin/activate
```

3. Install requirements.
```
pip install -r requirements.txt
```

4. Edit `config.py` with details of the database, path to csv and optionally ignored files.
```
USER = "postgres"
PASS = "123"
HOST = "127.0.0.1"
PORT = 5432
DB_NAME = "example_db"
CSV_DIR = "example_data"
IGNORED_FILES = []

```

5. Delete existing db if it exists.
```
psql -U postgres -h 127.0.0.1
DROP DATABASE pcdb_test;
\q
```

6. Create `example_db`.
```
psql -U postgres -h 127.0.0.1
CREATE DATABASE pcdb_test;
\q
```

7. Create tables. From root directory run:
```
psql postgres -h 127.0.0.1 -d pcdb_test -f pcdb.sql
```

8. From root directory run:
```
python import.py
```
