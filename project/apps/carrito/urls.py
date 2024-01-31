from django.contrib import admin
from django.urls import path
from apps.carrito.views import carrito

urlpatterns = [
    path("carrito/", carrito, name="carrito"),
]