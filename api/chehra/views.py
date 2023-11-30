from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.db import connection


def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM embeddings")
        row = cursor.fetchall()

    return JsonResponse({"row": row})


class RegisterFace: 
    def __init__(self) -> None:
        pass 
    
    def preprocess_image(self):
        pass 

    def crop_face_from_frame(self):
        pass 
    
    def validate_single_face(self):
        pass 

    def get_face_embeddings(self):
        pass 

    def push_embeddings_to_db(self):
        pass 

    def register(self):
        pass 

class VerifyFace:
    def __init__(self) -> None:
        pass

    def preprocess_image(self):
        pass 

    def get_face_embeddings(self):
        pass 

    def search_top_k_faces_in_db(self,  k):
        pass 

    def get_face_identity(self):
        pass 
