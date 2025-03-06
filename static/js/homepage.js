import "./base.js"

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

document.addEventListener("DOMContentLoaded", function () {
    logoMoving("logo_centre", 10, 5, 800);
    logoMoving("logo_front", 12, 4, 400);
    logoMoving("logo_back", 8, 6, 600);

    stars();
})


