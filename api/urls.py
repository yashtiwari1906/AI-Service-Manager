from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns =[
    path('', home, name='api.home'),
    path('chehra/',include('api.chehra.urls')),
    # path('user/',include('api.user.urls')),
    # path('booking/',include('api.booking.urls')),
    
    # path('user/', include('api.user.urls'))
]