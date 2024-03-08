from django.shortcuts import render, redirect, reverse
from babel.numbers import format_currency
import locale
import re
from django.http import HttpResponse

from productos.models import Producto

def carrito(request):
    ids_productos = request.COOKIES.get('carrito', '').split('%2C')
    cantidades = request.COOKIES.get('cantidades', '').split('%2C')
    modelos = request.COOKIES.get('modelos', '').split('%2C')
    validacion = False
    
    if ids_productos != ['']:
        validacion = True
        cookiesABorrar = []
        if len(ids_productos) == len(cantidades) == len(modelos):
            productos_carrito = []
            contador = '0'
            firsNum = '0'
            for id_producto, cantidad, modelo in zip(ids_productos, cantidades, modelos):
                try:
                    producto = Producto.objects.get(id=id_producto)
                    contador = str(firsNum) + '00'
                    firsNum = int(firsNum) + 1    
                    validacion = True
                    if not modelo:
                        modelo = "Unico"

                
                    productos_carrito.append({
                        'contador' : contador,
                        'producto': producto,
                        'cantidad': cantidad,
                        'modelo': modelo,
                    })
                except Producto.DoesNotExist: 
                    cookiesABorrar.append(firsNum)
                    contador = str(firsNum) + '00'
                    firsNum = int(firsNum) + 1    
                    validacion = False

            print("Antes de configurar las cookies:")
            print(ids_productos)
            print(cantidades)
            print(modelos)


            for i in reversed(cookiesABorrar):
                ids_productos.pop(int(i))
                cantidades.pop(int(i))
                modelos.pop(int(i))

            response = HttpResponse()
            response.set_cookie('carrito', '%2C'.join(ids_productos), max_age=604.800, secure=True, path='/')
            response.set_cookie('cantidades', '%2C'.join(cantidades), max_age=604.800, secure=True, path='/')
            response.set_cookie('modelos', '%2C'.join(modelos), max_age=604.800, secure=True, path='/')
            print("Después de configurar las cookies:")
            print(ids_productos)
            print(cantidades)
            print(modelos)
            rendered_content = render(request, 'carrito.html', {'productos_carrito': productos_carrito, 'validacion': validacion}).content
            response.content = rendered_content
            return response
            #return render(request, 'carrito.html', {'productos_carrito': productos_carrito, 'validacion': validacion})
        else:
            return render(request, 'carrito.html', {'validacion': validacion})
    else:
        return render(request, 'carrito.html', {'validacion': validacion})

def pago(request):
    ids_productos = request.COOKIES.get('carrito', '').split('%2C')
    cantidades = request.COOKIES.get('cantidades', '').split('%2C')
    modelos = request.COOKIES.get('modelos', '').split('%2C')
    forma_pago = request.COOKIES.get('formaDePago','')
    validacion = False

    if ids_productos != ['']:
        validacion = True
        if len(ids_productos) == len(cantidades) == len(modelos):
            productos_carrito = []
            contador = '000'
            for id_producto, cantidad, modelo in zip(ids_productos, cantidades, modelos):
                producto = Producto.objects.get(id=id_producto)
                
                
                if not modelo:
                    modelo = "Unico"
                
                productos_carrito.append({
                    'contador' : contador,
                    'producto': producto,
                    'cantidad': cantidad,
                    'modelo': modelo,
                })
                contador = int(contador) + 100
                
            return render(request, 'pago.html', {'productos_carrito': productos_carrito,'validacion': validacion, 'forma_pago' : forma_pago})
        else:
            return render(request, 'pago.html', {'validacion': validacion, })
    else:
        return render(request, 'pago.html', {'validacion': validacion, 'modelos': modelos})

