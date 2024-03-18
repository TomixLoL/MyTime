from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from productos.forms import ProductoForm, ImagenProductoFormSet, OpcionFormSet
from productos.models import Producto
from productos.forms import ProductoCategoriaForm


# Create your views here.
@login_required
def administracion(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        imagen_formset = ImagenProductoFormSet(request.POST, request.FILES, instance=Producto())
        opcion_formset = OpcionFormSet(request.POST, instance=Producto())

        if producto_form.is_valid() and imagen_formset.is_valid() and opcion_formset.is_valid():
            producto = producto_form.save()
            imagenes = imagen_formset.save(commit=False)
            for imagen in imagenes:
                imagen.producto = producto
                imagen.save()
            opciones = opcion_formset.save(commit=False)
            for opcion in opciones:
                opcion.producto = producto
                opcion.save()

            # Limpiar los formularios después de haberlos procesado exitosamente
            producto_form = ProductoForm()
            imagen_formset = ImagenProductoFormSet(instance=Producto())
            opcion_formset = OpcionFormSet(instance=Producto())
            return render(request, 'producto_admin.html', {
                'producto_form': producto_form,
                'imagen_formset': imagen_formset,
                'opcion_formset': opcion_formset
            })
    else:
        producto_form = ProductoForm()
        imagen_formset = ImagenProductoFormSet(instance=Producto())
        opcion_formset = OpcionFormSet(instance=Producto())
    return render(request, 'producto_admin.html', {
        'productos': productos,
        'producto_form': producto_form,
        'imagen_formset': imagen_formset,
        'opcion_formset': opcion_formset
    })


@login_required
def AdminCategoria(request):
    if request.method == 'POST':
        categoria_form = ProductoCategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect('AdminCategoria')  # Redirige a la página de productos después de agregar la categoría
    else:
        categoria_form = ProductoCategoriaForm()
    
    return render(request, 'categoria_admin.html', {'categoria_form': categoria_form})