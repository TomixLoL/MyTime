from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.ProductoListView.as_view(), name='index'),
]