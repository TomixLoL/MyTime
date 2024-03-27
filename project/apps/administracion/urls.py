from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    #Sesiones
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    #Listados del panel
    path("administracion-producto", views.AdminProducto, name="adm-producto"),
    path("administracion-categoria", views.AdminCategoria, name="adm-categoria"),
    path("administracion-estampado", views.AdminEstampado, name="adm-estampado"),
    path("administracion-usuario", views.AdminUsuario, name="adm-usuario"),
    #Modificaciones
    path("administracion-producto/editar/<int:pk>", views.ProductoEdit.as_view(), name="edit-producto"),
    path("administracion-categoria/editar/<int:pk>", views.CategoriaEdit.as_view(), name="edit-categoria"),
    path("administracion-estampado/editar/<int:pk>", views.EstampadoEdit.as_view(), name="edit-estampado"),
    path("administracion-usuario/editar/<int:pk>", views.UsuarioEdit, name="edit-usuario"),
]