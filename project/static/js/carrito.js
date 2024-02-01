const inputPago = document.getElementsByName('pago')

inputPago[0].addEventListener('click', ()=>{
    if(inputPago[1].checked){
        inputPago[1].checked = false
    }
})
inputPago[1].addEventListener('click', ()=>{
    if(inputPago[0].checked){
        inputPago[0].checked = false
    }
})



const totalAPagar = document.getElementById("totalPagar")
const preciosProd = document.getElementsByName('precioProductos')


let total = 0;

preciosProd.forEach((prod)=>{
    console.log(prod);
    console.log(total);
    if(total != 0){
        total = parseFloat(total.replace('$', '').replace('.',''))
    }
    total += parseFloat(prod.innerHTML.replace('$', '').replace('.',''))
    total = new Intl.NumberFormat("de-DE", { style: "currency", currency: "ARS" }).format(total)
    console.log(total);
})

totalAPagar.innerHTML = '$' + total.replace('ARS','')



