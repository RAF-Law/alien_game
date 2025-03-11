function stars(){
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
    stars();

    loginGlitching("login_bg",3,50);
})