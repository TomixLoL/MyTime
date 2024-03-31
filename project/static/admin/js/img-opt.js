let inputImgStandar = document.querySelectorAll('.input-imagenes');
let imgIndex = inputImgStandar.length
let maxImg = document.getElementById('id_imagenes-TOTAL_FORMS')
let btnImg = document.getElementById('setInputImgBtn')
let containerImg = document.getElementById('inputs-img-container')

//Obetener los botones eliminar
let deleteBtn = document.querySelectorAll('.btn-danger')

btnImg.addEventListener('click', (e) => {
    e.preventDefault()
    let newContainer = document.createElement('div')
    newContainer.classList.add('input-imagenes')
    newContainer.setAttribute('name', `imagenes-${imgIndex}`)
    let newInput = document.createElement('input')
    newInput.setAttribute('type', 'file')
    newInput.setAttribute('name', `imagenes-${imgIndex}-imagenes`)
    newInput.setAttribute('accept', 'image/')
    newInput.setAttribute('id', `id_imagenes-${imgIndex}-imagenes`)
    newContainer.appendChild(newInput)
    let newBtn = document.createElement('button')
    newBtn.innerHTML = 'Eliminar'
    newBtn.setAttribute('type', 'button')
    newBtn.setAttribute('class', 'btn btn-danger')
    newBtn.setAttribute('id', `imagenes-${imgIndex}`)
    newContainer.appendChild(newBtn)
    containerImg.appendChild(newContainer)
    maxImg.value = imgIndex + 1
    inputImgStandar = document.querySelectorAll('.input-imagenes');
    imgIndex = inputImgStandar.length
    SetDeleteBtn()
})

let inputOptStandar = document.querySelectorAll('.input-opciones');
let optIndex = inputOptStandar.length
let maxOpt = document.getElementById('id_opciones-TOTAL_FORMS')
let btnOpt = document.getElementById('setInputOptBtn')
let containerOpt = document.getElementById('inputs-opt-container')

btnOpt.addEventListener('click', (e) => {
    e.preventDefault()
    let newContainer = document.createElement('div')
    newContainer.classList.add('input-opciones')
    newContainer.setAttribute('name', `opciones-${optIndex}`)
    let newInput = document.createElement('input')
    newInput.setAttribute('type', 'text')
    newInput.setAttribute('name', `opciones-${optIndex}-opciones`)
    newInput.setAttribute('id', `id_opciones-${optIndex}-opciones`)
    newContainer.appendChild(newInput)
    let newBtn = document.createElement('button')
    newBtn.innerHTML = 'Eliminar'
    newBtn.setAttribute('type', 'button')
    newBtn.setAttribute('class', 'btn btn-danger')
    newBtn.setAttribute('id', `opciones-${optIndex}`)
    newContainer.appendChild(newBtn)
    containerOpt.appendChild(newContainer)
    maxOpt.value = optIndex + 1
    inputOptStandar = document.querySelectorAll('.input-opciones');
    optIndex = inputOptStandar.length
    SetDeleteBtn()
})

// function SetDeleteBtn() {
//     inputImgStandar = document.querySelectorAll('.input-imagenes');
//     inputOptStandar = document.querySelectorAll('.input-opciones');
//     optIndex = inputOptStandar.length
//     imgIndex = inputImgStandar.length
//     console.log('hola');
//     deleteBtn = document.querySelectorAll('.btn-danger')
//     for (let i = 0; i < deleteBtn.length; i++) {
//         deleteBtn[i].addEventListener('click', (e) => {
//             console.log('Se Ejecuto');
//             if (deleteBtn[i].id.split('-')[0] == 'imagenes') {
//                     let idImg = e.target.id
//                     let toDelete = document.getElementsByName(idImg)
//                     containerImg.removeChild(toDelete[0])
//                     setTimeout(() => {
                    
//                     }, 1000);
//                     inputImgStandar = document.querySelectorAll('.input-imagenes');
//                     for (let element = 0; element < inputImgStandar.length; element++) {
//                         let obj = inputImgStandar[element]
//                         obj.setAttribute('name',`imagenes-${element}`)
//                         obj.innerHTML = `
//                 <input type="file" name="imagenes-${element}-imagenes" accept="image/*" id="id_imagenes-${element}-imagenes">
//                 <button type="button" id="imagenes-${element}" class="btn  btn-danger">Eliminar</button>
//                 `
//                     }
//                 SetDeleteBtn()
//             }

//             else if (deleteBtn[i].id.split('-')[0] == 'opciones') {
//                 deleteBtn[i].addEventListener('click', (e) => {
//                     let idOpt = e.target.id


//                 })
//             }
//         })
//     }
// }

// SetDeleteBtn()

function SetDeleteBtn() {
    inputImgStandar = document.querySelectorAll('.input-imagenes');
    inputOptStandar = document.querySelectorAll('.input-opciones');
    optIndex = inputOptStandar.length
    imgIndex = inputImgStandar.length
    console.log('hola');
    deleteBtn = document.querySelectorAll('.btn-danger')
    for (let i = 0; i < deleteBtn.length; i++) {
        deleteBtn[i].addEventListener('click', handleDelete);
    }
}

function handleDelete(e) {
    if (e.target.id.split('-')[0] == 'imagenes') {
        let idImg = e.target.id
        let toDelete = document.getElementsByName(idImg)
        containerImg.removeChild(toDelete[0])
        maxImg.value = imgIndex - 1
        inputImgStandar = document.querySelectorAll('.input-imagenes');
        for (let element = 0; element < inputImgStandar.length; element++) {
            let obj = inputImgStandar[element]
            obj.setAttribute('name', `imagenes-${element}`)
            obj.firstElementChild.setAttribute('name',`imagenes-${element}-imagenes`)
            obj.firstElementChild.setAttribute('id', `id_imagenes-${element}-imagenes`)
            obj.lastElementChild.setAttribute('id',`imagenes-${element}`)
        }
        SetDeleteBtn();
    } else if (e.target.id.split('-')[0] == 'opciones') {
        let idOpt = e.target.id
        let toDelete = document.getElementsByName(idOpt)
        containerOpt.removeChild(toDelete[0])
        maxOpt.value = optIndex - 1
        inputOptStandar = document.querySelectorAll('.input-opciones');
        for (let element = 0; element < inputOptStandar.length; element++) {
            let obj = inputOptStandar[element]
            obj.setAttribute('name', `opciones-${element}`)
            obj.firstElementChild.setAttribute('name',`opciones-${element}-opciones`)
            obj.firstElementChild.setAttribute('id', `id_opciones-${element}-opciones`)
            obj.lastElementChild.setAttribute('id',`opciones-${element}`)
        }
        SetDeleteBtn();
    }
}

SetDeleteBtn();
