const inputPago = document.getElementsByName('pago')
const buttsCant = document.getElementsByClassName('000001')


inputPago[0].addEventListener('click', ()=>{
    if(inputPago[1].checked){
        inputPago[1].checked = false
    }else if(inputPago[0].checked == false){
        inputPago[0].checked = true
    }
})
inputPago[1].addEventListener('click', ()=>{
    if(inputPago[0].checked){
        inputPago[0].checked = false
    }else if(inputPago[1].checked == false){
        inputPago[1].checked = true
    }
})



const preciosBase = []
const totalAPagar = document.getElementById("totalPagar")
const preciosProd = document.getElementsByName('todos_los_precios')
const cantidadProd = document.getElementsByName('todas_las_cantidades')
const CheckOutProd = document.getElementsByName('productos_checkout')

let total = 0;

function obtenerPrecios(){
    preciosProd.forEach((producto)=>{
        preciosBase.push( parseFloat(producto.innerHTML.replace('$','').replace(/\./g ,'').replace(',', '.')))})

}

function multiplicarPrecios(){
    let count = 0
    preciosProd.forEach((producto)=>{
        let precio = preciosBase[count]
        let cantidad = parseInt(cantidadProd[count].innerHTML)
        let precioCantidad = precio * cantidad

        precioCantidad = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(precioCantidad)
        precioCantidad = precioCantidad.replace('ARS','').split('')
        precioCantidad.splice(-1)

        count += 1
        producto.innerHTML = '$' + precioCantidad.join('')
    })

    calcularTotal()
}


function calcularTotal(){
    total = 0
    preciosProd.forEach((prod)=>{
        if(total != 0){
            total = parseFloat(total.replace('$', '').replace(/\./g, "").replace(',', '.'))
        }
        total += parseFloat(prod.innerHTML.replace('$', '').replace(/\./g,''))
        total = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(total)
        totalAPagar.innerHTML = '$' + total.replace('ARS','')
    })
       
}

obtenerPrecios() //Setea en un array los precios base para usarlos todas las veces necesarias
multiplicarPrecios() //Utiliza los precios base y los multiplica por la cantidad necesaria



//Agrega funcionalidad a los botones + - y delete permitiendoles modificar tanto lo visual como las cookies
for (i = 0; i < buttsCant.length; i++){
    buttsCant[i].addEventListener('click', (e)=>{
        let inputCant = document.getElementById(e.target.name)
        if(e.target.id == 'sumarCant'){
            if(parseInt(inputCant.value) < 10){
                inputCant.value = parseInt(inputCant.value) + 1
                let cantModificar = getCookie('cantidades').split(',')
                let indexOfProd = e.target.name.split('')
                indexOfProd.splice(-2)
                cantModificar[indexOfProd] = inputCant.value
                setCookie('cantidades' , cantModificar, { secure : true , 'max-age' : max_age})  
                cantidadProd[indexOfProd].innerHTML = inputCant.value
                multiplicarPrecios()           
            }
        }else if (e.target.id == 'restarCant'){
            if(parseInt(inputCant.value) > 1){
                inputCant.value = parseInt(inputCant.value) - 1
                let cantModificar = getCookie('cantidades').split(',')
                let indexOfProd = e.target.name.split('')
                indexOfProd.splice(-2)
                cantModificar[indexOfProd] = inputCant.value
                setCookie('cantidades' , cantModificar, { secure : true , 'max-age' : max_age})   
                cantidadProd[indexOfProd].innerHTML = inputCant.value
                multiplicarPrecios()  
            }
        }else if (e.target.id == 'delete'){
            let contenedorProducto = document.getElementsByClassName(e.target.name)
            contenedorProducto[0].style.display = 'none'
            let indexOfProd = e.target.name.split('')
            indexOfProd.splice(-2)
            let carritoMod = getCookie('carrito').split(',')
            let cantidadMod = getCookie('cantidades').split(',')
            let modeloMod = getCookie('modelos').split(',')
            console.log( carritoMod, cantidadMod, modeloMod);

            carritoMod.splice(indexOfProd, 1)
            cantidadMod.splice(indexOfProd, 1)
            modeloMod.splice(indexOfProd, 1)
            setCookie('carrito' , carritoMod, { secure : true , 'max-age' : max_age})   
            setCookie('cantidades' , cantidadMod, { secure : true , 'max-age' : max_age})   
            setCookie('modelos' , modeloMod, { secure : true , 'max-age' : max_age})   
        
            //Borrar del CheckOut
            CheckOutProd[indexOfProd].style.display = 'none'
            preciosBase[indexOfProd] = 0
            location.reload()
            

        }

    })
}

const modelosFormatear = document.getElementsByName('modelos_formatear')

modelosFormatear.forEach((modelo)=>{
    modelo.innerHTML = modelo.innerHTML.replace(/\%20/g, ' ')
})