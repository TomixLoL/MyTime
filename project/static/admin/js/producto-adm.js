const butLook = document.getElementById('lookProducto')
const butPlus = document.getElementById('plusProducto')
const divLook = document.getElementById('productosVista')
const divPlus = document.getElementById('agregarForm')

butLook.addEventListener('click', ()=>{
    divLook.classList.add('mostrar')
    divPlus.classList.remove('mostrar')
})
butPlus.addEventListener('click', ()=>{
    divPlus.classList.add('mostrar')
    divLook.classList.remove('mostrar')
})


