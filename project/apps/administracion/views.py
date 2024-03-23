from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from productos.forms import ProductoForm, ImagenProductoFormSet, OpcionFormSet, ProductoCategoriaForm, EstampadoForm
from productos.models import Producto, ProductoCategoria, Estampado
from django.http import JsonResponse, HttpResponse


# Create your views here.
@login_required
def AdminProducto(request):
    productos = Producto.objects.all()
    producto_form = ProductoForm()
    imagen_formset = ImagenProductoFormSet(instance=Producto())
    opcion_formset = OpcionFormSet(instance=Producto())

    if request.method == 'POST':

        # Si se envió el formulario para crear un nuevo producto
        if 'crear_producto' in request.POST:
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
                return redirect('administracion:adm-producto')

        # Si se envió una solicitud para eliminar un producto
        elif 'eliminar_producto' in request.POST:   
            
            producto_id = request.POST.get('eliminar_producto')
            if producto_id:
                producto = Producto.objects.get(id=producto_id)
                producto.delete()
                return redirect('administracion:adm-producto')

        elif 'modificar_precio' in request.POST:
            producto_id = request.POST.get('producto_id')
            nuevo_precio = request.POST.get('nuevo_precio')
            if producto_id and nuevo_precio:
                try:
                    producto = Producto.objects.get(pk=producto_id)
                    producto.precio = nuevo_precio
                    producto.save()
                    return JsonResponse({'status': 'ok'})
                except Producto.DoesNotExist:
                    pass
            else:
                producto_form = ProductoForm(request.POST)
                if producto_form.is_valid():
                    producto_form.save()
                    return redirect('administracion:adm-producto')

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
    estampado_form = EstampadoForm()

    if request.method == "POST":
        estampado_form = EstampadoForm(request.POST, request.FILES)

        if 'crear_estampado' in request.POST:
            if estampado_form.is_valid():
                estampado_form.save()
                return redirect('administracion:adm-estampado')

        elif 'eliminar_estampado' in request.POST:
                estampado_id = request.POST.get('eliminar_estampado')
                if estampado_id:
                    estampado = Estampado.objects.get(id=estampado_id)
                    estampado.delete()
                    return redirect('administracion:adm-estampado')
    return render(request, 'estampado_admin.html', {'estampados': estampados, 'estampado_form': estampado_form})

@login_required
def AdminUsuario(request):
    usuarios = User.objects.all()
    usuario_form = UserCreationForm()

    if request.method == 'POST':
        if 'crear_usuario' in request.POST:
            usuario_form = UserCreationForm(request.POST)
            if usuario_form.is_valid():
                usuario_form.save()
                return redirect('administracion:adm-usuario')
        
        elif 'eliminar_usuario' in request.POST:
                user_id = request.POST.get('eliminar_usuario')
                if user_id:
                    user = User.objects.get(id=user_id)
                    user.delete()
                    return redirect('administracion:adm-usuario')
    return render(request, 'usuario_admin.html', {'usuario_form': usuario_form, 'usuarios': usuarios})