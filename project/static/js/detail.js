
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


const imgP = document.getElementById("prodImg")

window.addEventListener("click", (e)=>{
    if(e.target.classList.contains("posibleImg")){
        let imag = e.target.src 
        imgP.src = imag;
    }
})