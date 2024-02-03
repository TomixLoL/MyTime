from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Producto, ProductoCategoria, Opcion, Estampado
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

from django.db.models import Q
from django.views.generic import ListView
from .models import Producto, ProductoCategoria

class ProductoListView(ListView):
    model = Producto
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('buscar', '')
        categoria_id = self.request.GET.get('categoria', '')

        if search_query:
            queryset = queryset.filter(
                Q(nombre__icontains=search_query) |
                Q(descripcion__icontains=search_query)
            ).distinct()

        if categoria_id:
            queryset = queryset.filter(categoria=categoria_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset'] = self.request.GET.get('buscar', '')
        context['categoria_seleccionada'] = self.request.GET.get('categoria', '')
        context['categorias'] = ProductoCategoria.objects.all()
        context['productos_destacados'] = Producto.objects.filter(destacado=True)
        context['productos_opciones'] = Producto.objects.filter()

        if not context['object_list']:
            context['no_resultados'] = "No hay productos con esas características."

        return context

    def get(self, request, *args, **kwargs):
        # Antes de procesar la solicitud, verificamos si se ha cambiado la categoría
        categoria_anterior = request.session.get('categoria_seleccionada', '')
        nueva_categoria = request.GET.get('categoria', '')

        if categoria_anterior != nueva_categoria:
            # La categoría ha sido cambiada, eliminamos la búsqueda
            request.session['categoria_seleccionada'] = nueva_categoria
            request.GET = request.GET.copy()  # Copiamos el QueryDict para que sea mutable
            request.GET['buscar'] = ''  # Establecemos la búsqueda en blanco
            request._get = None  # Forzamos la reconstrucción del QueryDict

        return super().get(request, *args, **kwargs)


def estampados(request):
    model = Estampado
    estampados = Estampado.objects.all()

    return render(request, 'estampados.html' , { 'estampados' : estampados})