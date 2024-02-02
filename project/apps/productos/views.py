from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Producto, ProductoCategoria, Opcion
from django.db.models import Q
from django.shortcuts import render

from . import models


class ProductoDetail(DetailView):
    model = models.Producto
    template_name = 'producto_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtén el producto actual
        producto_actual = self.get_object()

        # Verifica si hay opciones para el producto actual
        opciones_disponibles = producto_actual.opciones.exists()
        
        # Agrega las opciones al contexto solo si existen
        if opciones_disponibles:
            context['opciones'] = producto_actual.opciones.all()
            context['opciones_disponibles'] = producto_actual.opciones.exists()

        return context
class ProductoListView(ListView):
    # Define la clase para mostrar una lista de productos
    model = Producto  # Utiliza el modelo Producto para esta vista
    template_name = 'index.html'  # La plantilla HTML asociada a esta vista

    def get_queryset(self):
        # Método que retorna el conjunto de datos (QuerySet) de productos a mostrar
        queryset = super().get_queryset()  # Obtiene el QuerySet base definido por el modelo
        search_query = self.request.GET.get('buscar', '')  # Obtiene el valor del parámetro 'buscar' de la URL
        categoria_id = self.request.GET.get('categoria', '')  # Obtiene el valor del parámetro 'categoria' de la URL

        if search_query:
            # Si hay un valor en 'buscar', filtra los productos por nombre o descripción
            queryset = queryset.filter(
                Q(nombre__icontains=search_query) |
                Q(descripcion__icontains=search_query)
            ).distinct()

        if categoria_id:
            # Si hay un valor en 'categoria', filtra los productos por esa categoría
            queryset = queryset.filter(categoria=categoria_id)

        return queryset  # Retorna el QuerySet resultante después de aplicar los filtros

    def get_context_data(self, **kwargs):
        # Método para agregar datos adicionales al contexto de la plantilla
        context = super().get_context_data(**kwargs)  # Obtiene el contexto base

        # Agrega las siguientes variables al contexto
        context['queryset'] = self.request.GET.get('buscar', '')  # Valor de 'buscar'
        context['categoria_seleccionada'] = self.request.GET.get('categoria', '')  # Valor de 'categoria'
        context['categorias'] = ProductoCategoria.objects.all()  # Todas las categorías disponibles
        context['productos_destacados'] = Producto.objects.filter(destacado=True)
        context['productos_opciones'] = Producto.objects.filter()

        return context  # Retorna el contexto actualizado con las variables adicionales
    
def estampados(request):
    hola = 1
    return render(request, 'estampados.html' , { 'hola' : hola})