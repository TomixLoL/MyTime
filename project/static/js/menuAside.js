let button = document.getElementById("menu");
let aside = document.getElementById("aside");
let path = document.getElementById("path");
let svg = document.getElementById("svg");
let clicked = false;

window.addEventListener('load', ()=>{
  button = document.getElementById("menu");
  aside = document.getElementById("aside");
  path = document.getElementById("path");
  svg = document.getElementById("svg");
  clicked = false;
})

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