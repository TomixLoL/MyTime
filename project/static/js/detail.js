let button = document.getElementById("menu");
let aside = document.getElementById("aside");
let path = document.getElementById("path");
let svg = document.getElementById("svg");
let clicked = false;


window.addEventListener("click", (e) => {

  if (!clicked) {
    if (e.target == button || e.target == path) {
      console.log(clicked);
      aside.style.display = "block"
      aside.style.display = "flex"
      clicked = !clicked
    }
  } else if (clicked) {
    if (!e.target.classList.contains("token-menu")) {
      console.log(clicked);
      clicked = !clicked
      aside.style.display = "none"
    } else if (e.target == button || e.target == button) {
      console.log(clicked);
      clicked = !clicked
      aside.style.display = "none"
    }
  }
})

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