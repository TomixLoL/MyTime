 // devuelve la cookie con el nombre dado,
// o undefined si no la encuentra

function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options = {}) {

    options = {
        path: '/',
        // agregar otros valores predeterminados si es necesario
        ...options
    };

    if (options.expires instanceof Date) {
        options.expires = options.expires.toUTCString();
    }

    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }
    document.cookie = updatedCookie;
}

function deleteCookie(name) {
    setCookie(name, "", {
        'max-age': -1
    })
}

try{
var numeroCarrito = document.getElementById("numeroCarrito");
}catch (e){
}
try{
var carrito  = "";
}catch(e){
}
try{
var cantidades = "";
}catch(e){
}
try{
var modelos = "";
}catch(e){
}


if(typeof max_age == undefined){
var max_age = 604.800
}



/*
    ESTO ES PARA LA PAGINA DE DETAILS, PARA PODER CARGAR LA INFORMACIÓN AL CARRITO
*/

try{
var formulario = document.getElementById("formulario")
var modal = document.getElementById("MODAL")
}catch(e){
}

if (formulario != null) {
	console.log('Capturo  algo')    
formulario.addEventListener("submit", (e) => {
        
	e.preventDefault();

        // capturamos los datos del formulario
        let formData = new FormData(formulario);
        let datos = [];

        // Mostramos las [claves, valores] capturados en consola
        for (var pair of formData.entries()) {
            datos.push(pair[0] + ':' + pair[1])
        }

        let idProducto = datos[0].split(":")[1]
        let cantidadProducto = datos[3].split(":")[1]
        let modeloProducto
        if (datos.length > 4){
            modeloProducto = datos[4].split(":")[1]
        }

        if (carrito == "") {
            carrito = [idProducto]
            cantidades = [cantidadProducto]
            modelos = [modeloProducto]
            numeroCarrito.innerHTML = carrito.length
        } else {
            carrito = [...carrito, idProducto]
            cantidades = [...cantidades, cantidadProducto]
            modelos = [...modelos, modeloProducto]
            numeroCarrito.innerHTML = carrito.length
        }
        setCookie("carrito", carrito, { secure: true, "max-age": max_age })
        setCookie("cantidades", cantidades, { secure: true, "max-age": max_age })
        setCookie("modelos", modelos, { secure: true, "max-age": max_age })
        modal.style.display = "flex"
        setTimeout(() => {
            modal.style.display = "none "
        }, 2000);
    })
}                       
/*
    ACA TERMINA EL APARTADO
*/




if (getCookie("used") == undefined) {
    setCookie('used', "true", { secure: true, 'max-age': 86.400 })
    setCookie("carrito", [""], { secure: true, "max-age": 86.400 })
    setCookie("cantidades", [""], { secure: true, "max-age": 86.400 })
    setCookie("modelos", [""], { secure: true, "max-age": 86.400 })

}
else if (getCookie("used") == "true" && getCookie("carrito") == "") {
    numeroCarrito.innerHTML = "0"
    carrito = ""
    cantidades = ""
    modelos = ""
    setCookie('used', "true", { secure: true, 'max-age': 86.400 })
    setCookie("carrito", [""], { secure: true, "max-age": 86.400 })
    setCookie("cantidades", [""], { secure: true, "max-age": 86.400 })
    setCookie("modelos", [""], { secure: true, "max-age": 86.400 })

}
else if (getCookie("used") == "true" && getCookie("carrito") != undefined) {
    carrito = getCookie("carrito").split(",")
    cantidades = getCookie("cantidades").split(",")
    modelos = getCookie("modelos").split(",")
    numeroCarrito.innerHTML = carrito.length

}


try{
var carritoForm = document.getElementById("carritoForm")
var butPagar = document.getElementById('botonPagar')
var formaDePago = '';
}catch(e){}

try {
	if (carritoForm != null) {
    	butPagar.addEventListener("click", (e) => {
        // capturamos los datos del formulario
        let formData = new FormData(carritoForm);
        let datos = [];

        // Mostramos las [claves, valores] capturados en consola
        for (var pair of formData.entries()) {
            datos.push(pair[0] + ':' + pair[1])

        }
        formaDePago = datos[0].split(':')[1]
        setCookie('formaDePago' , formaDePago , {secure : true, 'max-age' : max_age})
    })}
}
catch(e) {
}
