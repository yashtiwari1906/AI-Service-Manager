from django.urls import path, include
from rest_framework.authtoken import views
from .views import my_custom_sql

urlpatterns =[
    path('test/', my_custom_sql, name='api.home'),
    
]