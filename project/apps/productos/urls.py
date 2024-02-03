from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductoListView.as_view(), name='index'),
    path("productos/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("estampados/", views.Estampados, name='estampados'),
]