from django.shortcuts import render

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        # Obtener el carrito almacenado en la sesión o crear uno nuevo si no existe
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        # Agrega un producto al carrito
        id = str(producto.id)
        if id not in self.carrito.keys():
            # Si el producto no está en el carrito, lo agrega como un nuevo elemento
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            # Si el producto ya está en el carrito, aumenta la cantidad y actualiza el precio total
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio

        # Guarda el carrito actualizado en la sesión
        self.guardar_carrito()

    def guardar_carrito(self):
        # Guarda el carrito en la sesión y marca la sesión como modificada
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        # Elimina un producto del carrito
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]

        # Guarda el carrito actualizado en la sesión
        self.guardar_carrito()

    def restar(self, producto):
        # Reduce la cantidad de un producto en el carrito
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio

            # Si la cantidad llega a cero o menos, elimina el producto del carrito
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)

        # Guarda el carrito actualizado en la sesión
        self.guardar_carrito()

    def limpiar(self):
        # Elimina todos los productos del carrito
        self.session["carrito"] = {}
        self.session.modified = True

    def calcular_total(self):
        # Calcula el total sumando los precios acumulados de todos los productos en el carrito
        total = 0

        for item in self.carrito.values():
            total += item["acumulado"]

        return total
