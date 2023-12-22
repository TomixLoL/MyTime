from django.db import models
from babel.numbers import format_currency

class ProductoCategoria(models.Model):
    """Categorías de productos."""

    nombre = models.CharField(max_length=15, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    imagen_categoria = models.ImageField(upload_to="apps/productos/categoria-imagen/", verbose_name="imagen")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.nombre


class Producto(models.Model):
    """Productos que corresponden a una categoría."""

    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría")
    nombre = models.CharField(max_length=100)
    cantidad = models.FloatField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name="descripción")
    imagen_producto = models.ImageField(upload_to="apps/productos/producto-imagen/", verbose_name="imagen")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def precio_formateado(self):
        # Formatear el precio como moneda en formato argentino
        return format_currency(self.precio, 'ARS', locale='es_AR')

    def __str__(self):
        return f"{self.nombre} {self.precio_formateado()}"

