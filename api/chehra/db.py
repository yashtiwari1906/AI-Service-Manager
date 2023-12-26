from django.http import JsonResponse
from django.db import connection
from ai_service_manager.tasks import insert_into_DB

def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM embeddings")
        row = cursor.fetchall()

    return JsonResponse({"row": row})


class DBOperations:
    def __init__(self, table) -> None:
        self.table = table

    def insert(self, data_dict, async_insert = True):
        # with connection.cursor() as cursor:
        #     cursor.execute("insert into embeddingsStorage (id, name, embedding) values (1000, 'check', '[1, 2, 3]');")
        try: 
            if async_insert:
                insert_into_DB.delay(data_dict, self.table)
            else: 
                insert_into_DB(data_dict, self.table)

            return {"success": True, "msg": "Embeddings saved successfully."}
           

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

    def similarity_search_retireval(self, query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows