
const butPlus = document.getElementById("sumarCant")
const butLess = document.getElementById("restarCant")
const cantidad = document.getElementById("cant")

butPlus.addEventListener("click", (e)=>{
    e.preventDefault()
    if(cantidad.value < 10){
        cantidad.value = parseInt(cantidad.value) + 1 
    }
})

butLess.addEventListener("click", (e)=>{
    e.preventDefault()
    if(cantidad.value > 1){
        cantidad.value = parseInt(cantidad.value) - 1 
    }
})

cantidad.addEventListener("keyup", (e)=>{
    if (parseInt(cantidad.value) > 10){
        cantidad.value = 10
    }
    if (parseInt(cantidad.value) < 1){
        cantidad.value = 1
    }
})
const modal = document.getElementById("MODAL")

const formulario = document.getElementById("formulario")

formulario.addEventListener("submit", (e)=>{
    e.preventDefault();

    // capturamos los datos del formulario
    var formData = new FormData(formulario);
    let datos = [];

    // Mostramos las [claves, valores] capturados en consola
    for(var pair of formData.entries()) {
        datos.push(pair[0]+ ': '+ pair[1])
    }
    
    modal.style.display = "flex"
    setTimeout(() => {
    modal.style.display = "none "
    }, 2000);
})


const imgP = document.getElementById("prodImg")

window.addEventListener("click", (e)=>{
    if(e.target.classList.contains("posibleImg")){
        let imag = e.target.src 
        imgP.src = imag;
    }
})