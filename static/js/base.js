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

document.addEventListener("DOMContentLoaded", function () {
    loginGlitching("login_bg",3,50);
})