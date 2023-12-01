from django.http import JsonResponse
from django.db import connection


def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM embeddings")
        row = cursor.fetchall()

    return JsonResponse({"row": row})


class DBOperations:
    def __init__(self, table) -> None:
        self.table = table

    def insert(self, data_dict):
        # with connection.cursor() as cursor:
        #     cursor.execute("insert into embeddingsStorage (id, name, embedding) values (1000, 'check', '[1, 2, 3]');")
        try: 
            column_names = list(data_dict.keys()) 
            values = list(data_dict.values())
            id, name, embedding = 'id', 'name', 'embedding'
            query_str = f"insert into {self.table} ("+str(id)+','+str(name)+','+str(embedding)+f") values {tuple(values)}" #make a function and return a value
            # try:
            with connection.cursor() as cursor:
                cursor.execute(query_str)
            return {"success": True, "msg": "Embeddings saved successfully."}
            # except:
            #     return False 

        except Exception as e:
            raise Exception("Some error has occured during insertion check data_dict once", e)
        

    def retrieve(self, limit=None, condition=None):
        with connection.cursor() as cursor:
            if limit is None and condition is None: 
                cursor.execute(f"SELECT * FROM {self.table}")
                row = cursor.fetchall()
            elif condition is None:
                cursor.execute(f"SELECT * FROM {self.table} LIMIT {limit}")
                row = cursor.fetchall()
        
        return row 