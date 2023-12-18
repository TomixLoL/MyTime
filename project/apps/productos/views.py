from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Producto, ProductoCategoria
from django.db.models import Q

from . import forms, models

def index(request):
    #Buscador
    queryset = request.GET.get('buscar', '')
    productos = Producto.objects.filter(nombre__icontains = queryset)
    if queryset:
        # Filtra los productos por nombre
        productos = Producto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    return render(request, 'test.html', {'productos': productos, 'queryset': queryset})