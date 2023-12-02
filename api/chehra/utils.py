from django.db import connection

class UniqueIdGenerator:
    def __init__(self, table) -> None:
        self.table = table 

    def generate_uuid_for_vectorStorage(self):
        query = f"SELECT id from {self.table} ORDER BY id DESC LIMIT 1;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
        return int(row[0])

    def last_uuid_saved(self): 
        return self.generate_uuid_for_vectorStorage()
