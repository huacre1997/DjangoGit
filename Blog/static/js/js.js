// Variables

window.addEventListener('scroll', function () {
    menus();
});
let nav = document.getElementById("nav");

function menus() {
    let Desplazamiento_Actual = window.pageYOffset;

    if (Desplazamiento_Actual == 0) {
        nav.classList.remove("nav");
        nav.className = ("navhover ")
        nav.style.transition = '1s';
    } else {
        nav.classList.remove("nav");
        nav.className = ('navhover');
        nav.style.transition = '1s';


    }
}