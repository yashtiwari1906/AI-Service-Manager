from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.db import connection


def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM embeddings")
        row = cursor.fetchall()

    return JsonResponse({"row": row})
