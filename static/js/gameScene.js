import * as base from "./base.js";

export function updateWeapon(){
    const xmlString = localStorage.getItem("gameData");
    if (!xmlString) {
        console.log("No saved game found.");
        return null;
    }
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, "application/xml");
    const playerElement = xmlDoc.querySelector("Player");
    let weaponName = playerElement.querySelector("CurrentWeapon Name").textContent;
    if (weaponName!=="Fists"){
        fetch(`../../get_weapon_image/${weaponName}/`)  // Send request to Django backend
            .then(response => response.json())
            .then(data => {
                    document.getElementById("weapon").src = data.image_url;})
    }
}
//we no more need this
// const WEAPONS_LIST = { "Ak-47": 40,"Baseball Bat":15,"Laser Gun": 50,"Plasma Rifle": 60,"Energy Sword": 75,
//     "Flamethrower": 55,"Railgun": 90,"Katana": 100,"Chicken": 10,"Revolver": 25,"Shotgun": 45,}

// function updateTextXML(){

//     const xmlString = localStorage.getItem("gameData");
//     if (!xmlString) {
//         console.log("No saved game found.");
//         return null;
//     }
//     const parser = new DOMParser();
//     const xmlDoc = parser.parseFromString(xmlString, "application/xml");
//     const playerElement = xmlDoc.querySelector("Player");
//     let hp = playerElement.querySelector("HP").textContent;
//     let ap = playerElement.querySelector("AttackPoints").textContent;
//     let speed = playerElement.querySelector("Speed").textContent;
//     let food = playerElement.querySelector("Food").textContent;
//     let weapon = playerElement.querySelector("Weapon").textContent;
//     let damage = WEAPONS_LIST[weapon];
//     document.getElementById("hp").textContent = "HP: " + hp;
//     document.getElementById("ap").textContent = "Attack Points: " + ap;
//     document.getElementById("speed").textContent = "Speed: " + speed;
//     document.getElementById("food").textContent = "Food: " + food;
//     document.getElementById("damage").textContent = "Weapon Damage: " + damage;
// }

export function updateText(player,day){
    let hp = player.hp;
    let ap = player.attackPoints;
    let speed = player.speed;
    let food = player.food;
    let damage = player.currentWeapon.damage;
    let kill = player.enemiesKilled;
    document.getElementById("hp").textContent = "HP: " + hp;
    document.getElementById("ap").textContent = "Attack Points: " + ap;
    document.getElementById("speed").textContent = "Speed: " + speed;
    document.getElementById("food").textContent = "Food: " + food;
    document.getElementById("damage").textContent = "Weapon Damage: " + damage;
    document.getElementById("kill_num").textContent = kill;
    document.getElementById("survive_num").textContent = day;
}

document.addEventListener("DOMContentLoaded", function () {
    base.stars();
    base.scanning("info",20);
})