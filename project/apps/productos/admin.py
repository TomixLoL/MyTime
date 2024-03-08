from django.contrib import admin
from .models import Producto, ImagenProducto, ProductoCategoria, Opcion, Estampado

admin.site.site_title = "Administracion"
admin.site.site_header = "MyTime"

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class OpcionAdmin(admin.TabularInline):
    model = Opcion

@admin.register(ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "categoria",
        "nombre",
        "precio",
        "descripcion",
        "destacado",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "destacado",
        "categoria",
        "nombre",
    )
    list_filter = ("categoria", "destacado")
    inlines = [
        ImagenProductoAdmin,
        OpcionAdmin
    ]

@admin.register(Estampado)
class  EstampadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estampado_imagen')
