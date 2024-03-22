from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("administracion-producto", views.AdminProducto, name="adm-producto"),
    path("administracion-categoria", views.AdminCategoria, name="adm-categoria"),
    path("administracion-estampado", views.AdminEstampado, name="adm-estampado"),
    path("administracion-usuario", views.AdminEstampado, name="adm-usuario"),
]