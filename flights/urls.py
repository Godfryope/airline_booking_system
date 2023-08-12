from django.urls import path
from .views import *

urlpatterns = [
    path('', search_flights, name='search_flights'),
]