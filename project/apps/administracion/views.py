from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productos.forms import ProductoForm, ImagenProductoFormSet, OpcionFormSet, ProductoCategoriaForm, EstampadoForm
from productos.models import Producto, ProductoCategoria, Estampado
from django.http import JsonResponse


# Create your views here.
@login_required
def AdminProducto(request):
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
            return redirect('administracion:adm-producto')
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
    categorias = ProductoCategoria.objects.all()
    categoria_form = ProductoCategoriaForm()

    if request.method == 'POST':
        categoria_id = request.POST.get('categoria_id')
        nuevo_nombre = request.POST.get('nuevo_nombre')

        if categoria_id and nuevo_nombre:
            try:
                categoria = ProductoCategoria.objects.get(pk=categoria_id)
                categoria.nombre = nuevo_nombre
                categoria.save()
                return JsonResponse({'status': 'ok'})
            except ProductoCategoria.DoesNotExist:
                pass
        else:
            categoria_form = ProductoCategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('administracion:adm-categoria')

    return render(request, 'categoria_admin.html', {'categorias': categorias, 'categoria_form': categoria_form})

@login_required
def AdminEstampado(request):
    estampados = Estampado.objects.all()
    estampados_form = EstampadoForm()