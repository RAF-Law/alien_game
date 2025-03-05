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
    //if this stuff is found then it's authorised, otherwise it's not, so we call different functions
    let authorised = document.getElementById("login_bg_authorised");
    if (authorised){
        loginGlitching("login_bg_authorised");
    }else{
        loginGlitching("login_bg_unauthorised");
    }
})