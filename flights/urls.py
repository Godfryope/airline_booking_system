from django.urls import path
from .views import *

urlpatterns = [
    path('', search_seat, name='search_seat'),
]