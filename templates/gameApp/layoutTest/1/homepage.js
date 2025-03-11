function logoMoving(elementId, length, move, speed,direction) {
    let element = document.getElementById(elementId);
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

function stars(){ //random stars each time the page is loaded
    for (let i = 0; i < 50; i++) {
        let div = document.createElement("div");
        div.classList.add("star");
        
        div.style.position = "fixed";
        div.style.left = `${Math.random() * window.innerWidth}px`;
        div.style.top = `${Math.random() * window.innerHeight}px`;
        div.style.transform = `scale(${Math.random()})`;

        document.body.appendChild(div);
    }
}

function loginGlitching(elementId){
    let element = document.getElementById(elementId);
    let currentcolor = window.getComputedStyle(element).backgroundColor.match(/\d+/g).map(Number);
    //right, chatgpt taught me to get a numeric stuff like this, the format looks so evil
    //that match returns a string list and map turns it into integers
    let direction = 1;

    function colorchange(){
        let r = currentcolor[0]+direction*3;
        let g = currentcolor[1]+direction*3;
        let b = currentcolor[2]+direction*3;
        element.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
        direction *= -1;
    }

    setInterval(colorchange, 50);
}

document.addEventListener("DOMContentLoaded", function () {
    logoMoving("logo_centre", 10, 5, 800,-1);
    logoMoving("logo_front", 12, 4, 400,-1);
    logoMoving("logo_back", 8, 6, 600,-1);

    stars();

    loginGlitching("login_bg");
})