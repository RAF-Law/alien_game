import * as base from "./base.js";
function randomEffect(elementId,time){
    let parent = document.getElementById(elementId);
    function addRandomElement() {
        let newElement = document.createElement("div");
        newElement.classList.add("cube");

        let x = Math.random() * (parent.getBoundingClientRect().width*1.2);
        let y = Math.random() * (parent.getBoundingClientRect().height*1.1);
        let transparent = 1;
        let speed = Math.random()*3 + 1;
        newElement.style.left = `${parent.getBoundingClientRect().left*0.9+x}px`;
        newElement.style.top = `${parent.getBoundingClientRect().top*0.8+y}px`;
        newElement.style.width =`${parent.getBoundingClientRect().width*0.06}px`;
        newElement.style.height =`${parent.getBoundingClientRect().height*0.06}px`;
        newElement.style.transform = `scale(${Math.random()*0.7+0.4})`;
        
        document.body.appendChild(newElement);

        let movementInterval = setInterval(() => {
            let currentTop = parseFloat(newElement.style.top);
            newElement.style.top = `${currentTop - speed}px`;
            transparent -= 0.1;
            newElement.style.backgroundColor = `rgba(132, 245, 255, ${transparent})`
        }, 200);

        setTimeout(() => {
            clearInterval(movementInterval);
            newElement.remove();
        }, 2000);
    }

    setInterval(addRandomElement, time);
}

document.addEventListener("DOMContentLoaded", function () {
    base.stars();

    randomEffect("game_scene",200);
    randomEffect("game_creation",200);
})