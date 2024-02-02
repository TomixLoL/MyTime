

let productosBruto = document.getElementsByName('productos')
let formaPago = document.getElementById('formaPagoProducto').innerHTML.replace('%20', ' ')
let redirectWsp = document.getElementById('redirectWsp')
let productos = []


productosBruto.forEach((bruto) => {
    let producto = bruto.innerHTML.split(';')
    productos.push({
        nombre: producto[0],
        precio: producto[1],
        cantidad: producto[2],
        modelo: producto[3],
    })
})



function crearMensajeMostrado() {
    let display = document.getElementById('mensajeWhats')
    let msjProd = []
    let total = 0
    productos.forEach((producto) => {
        let prXcant = parseFloat(producto.precio.replace('$', "").replace('.', '').replace(',', '.')) * producto.cantidad
        total = total + prXcant
        prXcant = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(prXcant)

        msjProd.push(`(x${producto.cantidad}) ${producto.nombre}, Modelo: ${producto.modelo}. Precio: $${prXcant} </br>`)
    })
    total = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(total)
    let mensaje = `
        <b>Detalles del pedido:</b></br>
        ${msjProd.join('')}
        </br>
        <b>Forma de pago: </b>
        ${formaPago}</br> </br>
        <b>Forma de Envio:</b> A coordinar
        </br> </br>
        <b>Precio total:</b> $${total}
    `;

    display.innerHTML = mensaje

}

crearMensajeMostrado()

// %20 es un espacio
// %0A es un salto de linea
function crearMensajeWsp() {
    let display = document.getElementById('mensajeWhats')
    let msjProd = []
    let total = 0
    productos.forEach((producto) => {
        let prXcant = parseFloat(producto.precio.replace('$', "").replace('.', '').replace(',', '.')) * producto.cantidad
        total = total + prXcant
        prXcant = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(prXcant)

        msjProd.push(`(x${producto.cantidad}) ${producto.nombre}, Modelo: ${producto.modelo}. Precio: $${prXcant}</br>`)
    })
    total = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(total)
    let mensaje = `<b>Detalles del pedido:</b></br>${msjProd.join('')}</br><b>Forma de pago:</b> ${formaPago}</br> </br><b>Forma de Envio:</b> A coordinar</br> </br><b>Precio total:</b> $${total}
    `;
    mensaje = mensaje.replace(/ /gi, "%20").replace(/<\/br>/g, "%0A").replace(/<b>/g, '*').replace(/<\/b>/g, "*")

    
    console.log(mensaje);
    redirectWsp.href = `https://api.whatsapp.com/send?phone=541134661603&text=${mensaje}`
}

crearMensajeWsp()   

