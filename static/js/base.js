export function loginGlitching(elementId,variation,time){ //you need to export them to call them from other files
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

export function logoMoving(elementId, length, move, speed,direction) {
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

export function logoMovingTop(elementId, length, move, speed,direction) {
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

export function stars(){ //random stars each time the page is loaded
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

const secretCode = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowLeft", "ArrowRight", "ArrowLeft", "ArrowRight"];
let inputSequence = []; 

document.addEventListener("keydown", function(event) {
    inputSequence.push(event.key);

    if (inputSequence.length > secretCode.length) {
        inputSequence.shift();
    }

    if (JSON.stringify(inputSequence) === JSON.stringify(secretCode)) {
        loginUser();
        inputSequence = [];
    }
});

function loginUser() {
    window.location.href = easterEggUrl
}

document.addEventListener("DOMContentLoaded", function() {
    var music = document.getElementById("backgroundMusic");
    var musicToggle = document.getElementById("musicToggle");
    var musicIcon = musicToggle.querySelector("img");
    var musicOnPath = musicToggle.getAttribute("data-music-on");
    var musicOffPath = musicToggle.getAttribute("data-music-off");

    // Retrieve stored music state
    var musicPlaying = localStorage.getItem('musicPlaying') === 'true';
    var musicCurrentTime = parseFloat(localStorage.getItem('musicCurrentTime')) || 0;

    if (musicPlaying) {
        music.currentTime = musicCurrentTime;
        music.play().catch(err => console.warn("Autoplay blocked:", err));
        musicIcon.src = musicOnPath;
    } else {
        music.pause();
        musicIcon.src = musicOffPath;
    }
    window.addEventListener("beforeunload", function() {
        localStorage.setItem('musicCurrentTime', music.currentTime);
    });

    // moved the function here
    musicToggle.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default anchor behavior

        if (music.paused) {
            music.play();
            musicIcon.src = musicOnPath;
            localStorage.setItem('musicPlaying', 'true');
        } else {
            music.pause();
            musicIcon.src = musicOffPath;
            localStorage.setItem('musicPlaying', 'false');
        }

        localStorage.setItem('musicCurrentTime', music.currentTime);
    });
});

//scanning effect
export function scanning(elementId,gap){
    let element = document.getElementById(elementId);
    let position = gap/2;
    let positioncounter = 1;
    let direction = 1;
    const h = (parseInt(window.getComputedStyle(element).height)-gap) / 60;

    function strip(){
        let newElement = document.createElement("div");
        let transparent = 1;
        newElement.classList.add("strip");
        newElement.style.top = position + "px";
        newElement.style.height = h + "px";
        newElement.style.pointerEvents = "none"
        position = h * positioncounter;
        positioncounter += direction;
        element.appendChild(newElement);

        if (positioncounter > 60 || positioncounter <1){
            direction*=-1
        }

        let movementInterval = setInterval(() => {
            transparent -= 0.1;
            newElement.style.backgroundColor = `rgba(132, 245, 255, ${transparent})`
        }, 20);

        setTimeout(() => {
            clearInterval(movementInterval);
            newElement.remove();
        }, 200);
    }
    
    setInterval(strip, 30);
}

document.addEventListener("DOMContentLoaded", function () {
    loginGlitching("login_bg",3,50);
})