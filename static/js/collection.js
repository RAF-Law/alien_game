import * as base from "./base.js";

document.addEventListener("DOMContentLoaded", function () {
    base.stars();
    hide("artifacts");
    base.scanning("details",20);
})

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
    "3": "Epic",
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