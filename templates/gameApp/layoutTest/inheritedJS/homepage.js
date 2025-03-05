import "./base.js"

function logoMoving(elementId, length, move, speed) {
    let element = document.getElementById(elementId);
    let direction = -1;
    let step = 0;

    function movefunc() {
        let current = parseInt(window.getComputedStyle(element).bottom);
        element.style.bottom = (current + length * direction) + "px";
        step++;

        if (step >= move) {
            direction *= -1;  
            step = 0; 
        }
    }

    setInterval(movefunc, speed);
}

function stars(){

}

document.addEventListener("DOMContentLoaded", function () {
    logoMoving("logo_centre", 10, 5, 800);
    logoMoving("logo_front", 12, 4, 400);
    logoMoving("logo_back", 8, 6, 600);

    stars();
})


