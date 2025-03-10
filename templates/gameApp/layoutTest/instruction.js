function logoMoving(elementId, length, move, speed,direction) {
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

function loginGlitching(elementId,variation,time){
    let element = document.getElementById(elementId);
    let currentcolor = window.getComputedStyle(element).backgroundColor.match(/\d+/g).map(Number);
    let direction = 1;

    function colorchange(){
        let r = currentcolor[0]+direction*variation;
        let g = currentcolor[1]+direction*variation;
        let b = currentcolor[2]+direction*variation;
        element.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
        direction *= -1;
    }

    setInterval(colorchange, time);
}

document.addEventListener("DOMContentLoaded", function () {
    logoMoving("left_1", 10, 1, 500,-1);
    logoMoving("left_2", 12, 1, 500,1);
    logoMoving("left_3", 6, 2, 500,-1);
    logoMoving("right_1", 10, 1, 500,-1);
    logoMoving("right_2", 12, 1, 500,1);
    logoMoving("right_3", 6, 2, 500,-1);

    loginGlitching("login_bg",3,50);
})