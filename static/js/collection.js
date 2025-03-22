import * as base from "./base.js";

document.addEventListener("DOMContentLoaded", function () {
    base.stars();
    hide("artifacts");
    scanning("details",20);
})

//scanning effect
function scanning(elementId,gap){
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

//dynamically change rarity info
const colorMap = {
    "1": "white",
    "2": "rgb(94, 242, 217)",
    "3": "rgb(252, 210, 58)",
    "4": "rgb(181, 110, 216)",
    "6": "rgb(239, 42, 42)"
};
const nameMap = {
    "1": "Common",
    "2": "Rare",
    "3": "Legendary",
    "4": "Secret",
    "6": "?????",
}
function showItemDetail(object){
    let icon = document.getElementById("detail_icon");
    let name = document.getElementById("detail_name");
    let rarity = document.getElementById("detail_rarity");
    let description = document.getElementById("detail_description");
    let damage = document.getElementById("detail_damage");

    icon.src = object.querySelector(".icon").src;
    name.textContent = object.querySelector(".name").textContent;

    //change the number to something more intuitive
    rarity.textContent = object.querySelector(".rarity").textContent;
    rarity.style.color = colorMap[rarity.textContent.trim()];
    rarity.textContent = nameMap[rarity.textContent.trim()];

    description.textContent = object.querySelector(".description").textContent;

    if(object.querySelector(".damage")!=null){ //only weapons have this field
        damage.textContent = object.querySelector(".damage").textContent;
    }else{
        damage.textContent = "";
    }
}

function hide(elementId){
    let element = document.getElementById(elementId);
    element.style.display = "none";
}

let lastClicked = null;
document.addEventListener("click", function(event) { //click stuff
    if (event.target.classList.contains("itemcontainer")) {
        if (lastClicked && lastClicked !== event.target) {
            lastClicked.classList.remove("active");
        }
        event.target.classList.toggle("active");
        showItemDetail(event.target)
        lastClicked = event.target;
    }
});

let lastClickedCategory = null;
document.addEventListener("click", function(event) { //click stuff
    if (event.target.classList.contains("category")) {
        if (lastClickedCategory && lastClickedCategory !== event.target) {
            lastClicked.classList.remove("active");
        }
        if (event.target.id==="category_artifact"){
            hide("weapons");
            document.getElementById("artifacts").style.display = "flex";
        }else{
            hide("artifacts");
            document.getElementById("weapons").style.display = "flex";
        }
        lastClicked = event.target;
    }
});