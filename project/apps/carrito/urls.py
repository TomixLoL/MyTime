from django.contrib import admin
from django.urls import path
from apps.carrito.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

urlpatterns = [
    path("carrito/", tienda, name="carrito"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]