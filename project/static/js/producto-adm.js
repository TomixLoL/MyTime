const butLook = document.getElementById('lookProducto')
const butPlus = document.getElementById('plusProducto')
const divLook = document.getElementById('productosVista')
const divPlus = document.getElementById('agregarForm')

butLook.addEventListener('click', ()=>{
    divPlus.hidden = true
    divLook.hidden = false
})
butPlus.addEventListener('click', ()=>{
    divLook.hidden = true
    divPlus.hidden = false
})


