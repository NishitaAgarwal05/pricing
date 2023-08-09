from django.urls import path
from . import views

urlpatterns = [
    path('calculatefare/',views.calculate_fare)
]