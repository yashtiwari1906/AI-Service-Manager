from django.urls import path, include
from rest_framework.authtoken import views
from .views import my_custom_sql, register_face, verify_face

urlpatterns =[
    path('test/', my_custom_sql, name='api.home'),
    path('register-face/', register_face, name='api.chehra'),
    path('verify-face/', verify_face, name='api.home'),
    
]