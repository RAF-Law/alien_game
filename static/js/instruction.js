import "./base.js"

function logoMovingP(elementId, length, move, speed,direction) {
    let element = document.getElementById(elementId);
    let step = 0;

    function movefunc() {
        let current = parseInt(window.getComputedStyle(element).top);
        element.style.top = (current + length * direction) + "px";
        step++;

        if (step >= move) {
            direction *= -1;  
            step = 0; 
        }
    }

    setInterval(movefunc, speed);
}

document.addEventListener("DOMContentLoaded", function () {
    logoMovingP("left_1", 10, 1, 500,-1);
    logoMovingP("left_2", 12, 1, 500,1);
    logoMovingP("left_3", 6, 2, 500,-1);
    logoMovingP("right_1", 10, 1, 500,-1);
    logoMovingP("right_2", 12, 1, 500,1);
    logoMovingP("right_3", 6, 2, 500,-1);
})