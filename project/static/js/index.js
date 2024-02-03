const selectCategoria = document.getElementById('categoria')
const buscador = document.getElementById('bienvenida-buscador')

selectCategoria.addEventListener('change',(e)=>{
    e.preventDefault()
    buscador.value = ''
    this.form.submit()
})

