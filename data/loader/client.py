import json
import psycopg2
from psycopg2.extras import RealDictCursor

class PostgreSqlClient:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )

    def insert(self, query):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        self.connection.commit()

    def get_json_response(self, query):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        self.connection.commit()
        res = cursor.fetchall()
        cursor.close()
        return json.dumps(res)
