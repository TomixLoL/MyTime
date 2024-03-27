from django.urls import path
from apps.carrito.views import carrito, pago

urlpatterns = [
    path("carrito/", carrito, name="carrito"),
    path("pago/", pago, name="pago"),
]