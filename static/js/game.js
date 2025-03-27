import { updateText, updateWeapon } from "./gameScene.js";

let isEnterKeyPressed = false;

const WEAPONS_LIST = [
    { name: "Ak-47", description: "A powerful assault Rifle", damage: 40, attackMessage: "You shoot the alien with your Ak-47", rarity: 2 },
    { name: "Baseball Bat", description: "A wooden baseball bat with barbed wire wrapped around it", damage: 15, attackMessage: "You hit the alien with your gruesome baseball bat", rarity: 1 },
    { name: "Laser Gun", description: "A futuristic laser weapon not of this world", damage: 50, attackMessage: "You zap the alien with your Laser Gun", rarity: 2 },
    { name: "Plasma Rifle", description: "A high-tech energy charged rifle", damage: 60, attackMessage: "You blast the alien with your Plasma Rifle", rarity: 3 },
    { name: "Energy Sword", description: "A sword made of pure energy that emits a loud hum", damage: 75, attackMessage: "You slash the alien with your Energy Sword", rarity: 3 },
    { name: "Flamethrower", description: "A weapon that shoots flames, incinerating enemies", damage: 55, attackMessage: "You burn the alien with your Flamethrower", rarity: 2 },
    { name: "Railgun", description: "A powerful electromagnetic weapon that can fire from up to 65 kilometres away", damage: 90, attackMessage: "You blow a hole through the alien with your Railgun", rarity: 3 },
    { name: "Katana", description: "A katana that was passed down through many generations of honorable samurai", damage: 100, attackMessage: "You slice through the alien with unheavenly precision", rarity: 4 },
    { name: "Chicken", description: "A chicken that attacks aliens for some reason", damage: 10, attackMessage: "You throw the chicken at the alien", rarity: 1 },
    { name: "Revolver", description: "A six-shooter revolver", damage: 25, attackMessage: "You shoot the alien with your revolver", rarity: 1 },
    { name: "Shotgun", description: "A shotgun that fires a spread of pellets", damage: 45, attackMessage: "You blast the alien with your shotgun", rarity: 2 },
    { name: "Fists", description: "You fight with the alien, empty-handed", damage: 0, attackMessage: "You punch the alien.", rarity: 4 }, //sometimes after loading xml you lost punching text, so I add it here
];

const ARTIFACTS_LIST = [
    { name: "Cosmic Crystal", description: "A crystal that glows with an otherworldly light", rarity: 3 },
    { name: "Galactic Map", description: "A map showing the locations of alien worlds", rarity: 2 },
    { name: "Alien Artifact", description: "An artifact of unknown origin and purpose", rarity: 1 },
    { name: "Extraterrestrial Coin", description: "A coin from an alien currency", rarity: 1 },
    { name: "Space Helmet", description: "A helmet worn by an alien astronaut", rarity: 2 },
    { name: "Alien Skull", description: "The skull of a long-dead alien", rarity: 3 },
    { name: "Stardust", description: "A handful of glowing stardust", rarity: 1 },
    { name: "Meteorite Fragment", description: "A fragment of a meteorite", rarity: 2 },
    { name: "Alien Fossil", description: "A fossilized alien creature", rarity: 3 },
    { name: "Space Gem", description: "A gem from outer space", rarity: 2 },
    { name: "Alien Egg", description: "An egg containing an alien lifeform", rarity: 1 },
    { name: "Cosmic Dust", description: "A small amount of cosmic dust", rarity: 1 },
    { name: "Alien Amulet", description: "An amulet with alien symbols", rarity: 2 },
    { name: "Galactic Artifact", description: "An artifact from another galaxy", rarity: 3 },
    { name: "Space Relic", description: "A relic from outer space", rarity: 2 },
    { name: "Alien Crystal", description: "A crystal with alien properties", rarity: 3 },
    { name: "Extraterrestrial Relic", description: "A relic from an extraterrestrial civilization", rarity: 2 },
    { name: "Shimschnar's Left Hand Glove", description: "The left hand glove of the legendary alien warrior Shimschnar, it's true ability is unknown", rarity: 4 },
    { name: "The Dictionary of the Ancients", description: "A book containing the language of an ancient alien civilization", rarity: 4 },
    { name: "The Orb of Time", description: "An orb that can manipulate time itself, but you have no idea how it works", rarity: 4 },
];

function fetchWeapons() {
    const weapons = {};
    for (const weaponData of WEAPONS_LIST) {
        const weapon = new Weapon(
            weaponData.name,
            weaponData.description,
            weaponData.damage,
            weaponData.attackMessage,
            weaponData.rarity
        );
        weapons[weapon.name] = weapon;
    }
    return weapons;
}

function fetchArtifacts() {
    const artifacts = {};
    for (const artifactData of ARTIFACTS_LIST) {
        const artifact = new Artifact(
            artifactData.name,
            artifactData.description,
            artifactData.rarity
        );
        artifacts[artifact.name] = artifact;
    }
    return artifacts;
}

const RARITIES = { 1: "Common", 2: "Rare", 3: "Epic", 4:"Secret" };

class Weapon {
    constructor(name, description, damage, attackMessage, rarity) {
        this.name = name;
        this.description = description;
        this.damage = damage;
        this.attackMessage = attackMessage;
        this.rarity = rarity;
    }

    showAttackMessage() {
        printMessage(this.attackMessage);
    }

    toString() {
        return `${this.name} - ${this.description} (${this.damage} damage) | ${RARITIES[this.rarity]} |`;
    }
}

class Artifact {
    constructor(name, description, rarity) {
        this.name = name;
        this.description = description;
        this.rarity = rarity;
    }

    toString() {
        return `${this.name} - ${this.description} | ${RARITIES[this.rarity]} |`;
    }
}

const WEAPONS = fetchWeapons();
const ARTIFACTS = fetchArtifacts();

const ALIEN_WEAPONS = {
    "Goppin": new Weapon("Goppin", "A weapon that fires plasma.", 5, "The alien shoots you with plasma.", 1),
    "Sponk": new Weapon("Sponk", "A weapon that fires energy bursts.", 15, "The alien blasts you with energy.", 2),
    "Zorblax": new Weapon("Zorblax", "A weapon that shoots energy beams.", 25, "The alien fires a beam at you.", 3),
};

const ALIEN_NAMES = ["Zog", "Gorp", "Prip", "Geggin", "Nairn", "Hojjim", "Kada", "Rango"];

let endGame = false;
let day = 1;
let difficulty = 1;
let currentRoomCount = 0;

let map = {
    street: "street",
    emptyHouses: new Set(),
};

for (let i = 1; i <= 10; i++) {
    map[`house ${i}`] = { emptyRooms: new Set(), timesEntered: 0 };
}

const messagesDiv = document.getElementById("messages");
const inputField = document.getElementById("input");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function printMessage(message) {
    const messageElement = document.createElement("div");
    messageElement.className = "message";
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to the latest message
    updateText(player,day); //update everytime there's text change. not the best way but I cba to do anymore
    updateWeapon(); //update weapon image
    return new Promise(resolve => setTimeout(resolve, 100));
}

function getInput() {
    return inputField.value.trim();
}

function clearInput() {
    inputField.value = "";
}

class Room {
    constructor(roomType, alien = null) {
        this.loot = new Set();
        this.roomType = roomType;
        this.alien = alien;
    }

    generateLoot(items, rarityCap) {
        const lootNum = Math.floor(Math.random() * 2) + 1; // 1 to 2 items
        const itemArray = Object.values(items);

        for (let i = 0; i < lootNum; i++) {
            const randomIndex = Math.floor(Math.random() * itemArray.length);
            const item = itemArray[randomIndex];

            if (item.rarity <= rarityCap && !this.lootContains(item)) {
                this.loot.add(item);
            }
        }
    }

    lootContains(item) {
        for (const lootItem of this.loot) {
            if (lootItem.name === item.name) return true;
        }
        return false;
    }

    async searchRoom(player) {
        switch (this.roomType) {
            case 0:
                await printMessage("This room is empty.");
                break;
            case 1:
                this.generateLoot(WEAPONS, (Math.floor(Math.random() * 3) + 1));
                await this.handleLoot(player, "weapon");
                this.roomType = 0;
                break;
            case 2:
                this.generateLoot(ARTIFACTS, (Math.floor(Math.random() * 3) + 1));
                await this.handleLoot(player, "artifact");
                this.roomType = 0;
                break;
            case 3:
                if (this.alien === null) {
                    this.alien = createAlien();
                }
                await new Battle(player, this.alien).encounter();
                if (this.alien.hp == 0){
                    this.roomType = 0;
                }
                break;
            default:
                await printMessage("Invalid room type.");
                break;
        }
    }

    async handleLoot(player, lootType) {
        await printMessage(`You find yourself in a room filled with ${lootType}s.`);

        await sleep(1000);
        await printMessage("You search the room and find:");

        await sleep(1000);
        const lootArray = Array.from(this.loot);
        for (let i = 0; i < lootArray.length; i++) {
            await printMessage(`${i + 1}: ${lootArray[i]}`);
            await sleep(1000);
        }

        if (lootArray.length === 0) {
            await printMessage("Nothing of value.");
            return;
        }

        await printMessage("Would you like to take any of these items? (yes/no)");

        const getChoice = async () => {
            const userInput = getInput().toLowerCase().trim();
            clearInput();

            if (!["yes", "no", "q", "y", "n"].includes(userInput)) {
                await printMessage("Invalid input. Enter 'yes', 'no', or 'q' to quit.");
                return await getChoiceListener();
            }

            return userInput;
        };

        const getChoiceListener = () => {
            return new Promise(resolve => {
                const handleKeyPress = (event) => {
                    if (event.key === "Enter" && !isEnterKeyPressed) {
                        isEnterKeyPressed = true;
                        resolve(getChoice());
                        event.preventDefault();
                        document.removeEventListener("keydown", handleKeyPress); 
                    }
                };
        
                document.addEventListener("keydown", handleKeyPress);
            });
        };

        document.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                isEnterKeyPressed = false;
            }
        });

        const choice = await getChoiceListener();

        switch (choice) {
            case "yes":
            case "y":
                await printMessage(`Which ${lootType} would you like to take?`);

                const getItemChoice = async () => {
                    const choiceInput = getInput();
                    clearInput();

                    try {
                        const itemIndex = parseInt(choiceInput) - 1;
                        if (itemIndex >= 0 && itemIndex < lootArray.length) {
                            const selectedItem = lootArray[itemIndex];
                            if (lootType === "weapon") {
                                player.currentWeapon = selectedItem;
                                player.inventory.add(selectedItem); //we still need a copy in inventory to make sure it gets into collections
                            } else {
                                player.inventory.add(selectedItem);
                            }
                            await printMessage(`You now have ${selectedItem.name}.`);
                            player.food -= 1;
                            await printMessage("It cost you 1 Food.");
                            if (player.food <= 0){
                                await printMessage("Not being able to find enough food, you starve and die in desperation.");
                                await gameOver();
                            }
                        } else {
                            await printMessage("Invalid selection.");
                        }
                    } catch (error) {
                        await printMessage("Invalid selection.");
                    }
                };

                const getItemChoiceListener = () => {
                    return new Promise(resolve => {
                        const handleKeyPress = (event) => {
                            if (event.key === "Enter" && !isEnterKeyPressed) {
                                isEnterKeyPressed = true;
                                getItemChoice().then(resolve);
                                event.preventDefault();
                                document.removeEventListener("keydown", handleKeyPress);
                            }
                        };
                
                        document.addEventListener("keydown", handleKeyPress);
                    });
                };

                document.addEventListener("keyup", function(event) {
                    if (event.key === "Enter") {
                        isEnterKeyPressed = false;
                    }
                });

                await getItemChoiceListener();
                break; 

            case "no":
            case "n":
                await printMessage("You decide not to take any items.");
                break;

            case "q":
                endGame = true;
                break;

            default:
                await this.handleLoot(player, lootType);
                break;
        }
    }
}

class Alien {
    constructor(name, hp, weapon, speed) {
        this.name = name;
        this.hp = hp;
        this.weapon = weapon;
        this.speed = speed;
    }
}

class Player {
    constructor(hp, attackPoints, speed, food, location) {
        this.hp = hp;
        this.maxhp = hp;
        this.attackPoints = attackPoints;
        this.currentWeapon = new Weapon("Fists", "Your fists", 0, "You punch the alien.", 1);
        this.inventory = new Set();
        this.speed = speed;
        this.food = food;
        this.location = location;
        this.enemiesKilled = 0;
        this.secretsFound = {
            "The Orb of Time": false,
            "The Glove of Power": false,
            "Katana" : false,
            "Dictionary" : false,
        };
    }

    maxHPUpdate(){
        if (this.hp > this.maxhp){
            this.maxhp = this.hp
        }
    }

    toString() {
        return `HP: ${this.hp} | Attack Points: ${this.attackPoints} | Speed: ${this.speed} | Food: ${this.food}`;
    }

    async move(house) {
        const houseKey = `house ${house}`;

        if (map.emptyHouses.has(houseKey)) {
            await printMessage("This house is empty.");
            return;
        }

        map[houseKey].timesEntered += 1;

        if (map[houseKey].timesEntered === 5 && !this.secretsFound["The Orb of Time"]) {
            await printMessage("You have spent so much time in this house that you find a hidden artifact!");
            await sleep(1000);
            this.inventory.add(ARTIFACTS["The Orb of Time"]);
            await printMessage(`You now have ${ARTIFACTS["The Orb of Time"]}.`);
            this.secretsFound["The Orb of Time"] = true;
        } else {
            await printMessage(`You enter ${houseKey}.`);
            await printMessage("----------");
            await this.exploreHouse(houseKey);
        }
    }

    async exploreHouse(houseKey) {
        let numRooms = null;
        if (Object.keys(map[houseKey]).length <= 2){
            numRooms = Math.floor(Math.random() * 5) + 2; // 2 to 6 rooms
        }
        else{
            numRooms = Object.keys(map[houseKey]).length - 2;
        }

        if (map[houseKey].emptyRooms.size === numRooms) {
            await printMessage("All rooms in this house are empty.");
            return;
        }
        if (Object.keys(map[houseKey]).length <= 2){
            for (let i = 1; i <= numRooms; i++) {
                const roomKey = `room ${i}`;
                const roomType = Math.floor(Math.random() * 3) + 1; // 1 to 3
                map[houseKey][roomKey] = new Room(roomType);
            }
        }

        await printMessage(`There are ${numRooms} rooms in this house. Which room would you like to enter?`);

        const getRoomChoice = async () => {
            const roomInput = getInput();
            clearInput();

            try {
                const roomNum = parseInt(roomInput);
                if (roomNum >= 1 && roomNum <= numRooms) {
                    return roomNum;
                } else {
                    await printMessage(`Invalid input. Enter a number between 1 and ${numRooms}.`);
                    return null;
                }
            } catch (error) {
                await printMessage(`Invalid input. Enter a number between 1 and ${numRooms}.`);
                return null;
            }
        };

        let roomNum = null;
        while (roomNum === null) {
            await new Promise(resolve => {
                const handleKeyPress = (event) => {
                    if (event.key === "Enter" && !isEnterKeyPressed) {
                        isEnterKeyPressed = true;
                        getRoomChoice().then(num => {
                            roomNum = num;
                            resolve();
                        });
                        event.preventDefault();
                        document.removeEventListener("keydown", handleKeyPress); 
                    }
                };
        
                document.addEventListener("keydown", handleKeyPress);
            });
        }

        document.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                isEnterKeyPressed = false;
            }
        });

        const roomKey = `room ${roomNum}`;

        await printMessage(`You enter room ${roomNum}.`);
        await printMessage("-----");
        this.location = map[houseKey][roomKey];
        await this.location.searchRoom(this);
        if(this.hp > 0 && this.food > 0){ //sometimes it's saved after reset and it causes errors
            saveToXML(this);
        }

        if (!map[houseKey].emptyRooms.has(roomKey) && map[houseKey][roomKey].roomType == 0){
            map[houseKey].emptyRooms.add(roomKey);
        }

        currentRoomCount += 1;
        if (currentRoomCount >= 8) { //sometimes the day increment was delayed. now fixed
            day += 1;
            player.food -= 1;
            difficulty += 1;
            currentRoomCount -= 8;
            await printMessage(`It is now day ${day}. You eat something, rest and gain 20 HP.`);
            player.hp += 20;
            player.maxHPUpdate();
            if (player.food <= 0){
                await printMessage("Not being able to find enough food, you starve and die in desperation.");
                await gameOver();
            }
        }

        await printMessage("Would you like to leave the house? (yes/no)");

        const getLeaveChoice = async () => {
            const input = getInput().toLowerCase().trim();
            clearInput();

            if (!["yes", "no", "y", "n"].includes(input)) {
            await printMessage("Invalid input. Enter 'yes' or 'no'.");
            return await getLeaveChoiceListener();
            }

            return input;
        };

        const getLeaveChoiceListener = () => {
            return new Promise(resolve => {
                const handleKeyPress = (event) => {
                    if (event.key === "Enter" && !isEnterKeyPressed) {
                        isEnterKeyPressed = true;
                        resolve(getLeaveChoice());
                        event.preventDefault();
                        document.removeEventListener("keydown", handleKeyPress); 
                    }
                };
        
                document.addEventListener("keydown", handleKeyPress);
            });
        };

        document.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                isEnterKeyPressed = false;
            }
        });

        const leaveChoice = await getLeaveChoiceListener();

        if (leaveChoice === "no" || leaveChoice === "n") {
            await this.exploreHouse(houseKey);
        }
        if (map[houseKey].emptyRooms.size == numRooms && !map.emptyHouses.has(houseKey)) {
            map.emptyHouses.add(houseKey);
        }
    }
}

class Battle {
    constructor(player, alien) {
        this.player = player;
        this.alien = alien;
    }

    async fight() {
        while (this.player.hp > 0 && this.alien.hp > 0) {
            if (Math.floor(Math.random() * (this.player.speed + this.alien.speed)) < this.player.speed) {
                await this.playerAttack();

                if (this.alien.hp > 0) {
                    await this.alienAttack();
                }
            } else {
                await this.alienAttack();

                if (this.player.hp > 0) {
                    await this.playerAttack();
                }
            }

            await sleep(1000);
            await printMessage(`You: ${this.player.hp} HP`);
            await printMessage(`${this.alien.name}: ${this.alien.hp} HP`);
            await printMessage("-");
        }

        if (this.alien.hp <= 0) {
            await this.handleVictory();
        } else {
            await this.handleDefeat();
        }
    }

    async handleVictory() {
        await printMessage(`You killed ${this.alien.name}!`);
        this.player.hp += 20;
        this.player.attackPoints += 5;
        this.player.speed += 5;
        this.player.food += 1;
        this.player.enemiesKilled += 1;
        this.alien.hp = 0;
        this.player.maxHPUpdate();

        if (Math.floor(Math.random() * 30) === 21 && !this.player.secretsFound["The Glove of Power"]) {
            await printMessage("You find a mysterious glove!");
            this.player.inventory.add(ARTIFACTS["Shimschnar's Left Hand Glove"]);
            await printMessage(`You now have ${ARTIFACTS["Shimschnar's Left Hand Glove"]}.`);
            this.player.secretsFound["The Glove of Power"] = true;
        }
    }

    async handleDefeat() {
        await printMessage("You have been defeated.");
        await gameOver();
    }

    async encounter() {
        await printMessage(
            `You encounter an alien named ${this.alien.name}.\n` +
            `${this.alien.name} has a ${this.alien.weapon}.\n` +
            "What would you like to do? (attack/run)"
        );

        const getChoice = async () => {
            const userInput = getInput().toLowerCase().trim();
            clearInput();

            if (["attack", "run", "a", "r"].includes(userInput)) {
                return userInput;
            } else {
                await printMessage("Invalid input. Enter 'attack' or 'run'.");
                return null;
            }
        };

        let action = null;
        while (action === null) {
            await new Promise(resolve => {
                const handleKeyPress = (event) => {
                    if (event.key === "Enter" && !isEnterKeyPressed) {
                        isEnterKeyPressed = true;
                        getChoice().then(choice => {
                            action = choice;
                            resolve();
                        });
                        event.preventDefault();
                        document.removeEventListener("keydown", handleKeyPress);
                    }
                };
        
                document.addEventListener("keydown", handleKeyPress);
            });
        }

        document.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                isEnterKeyPressed = false;
            }
        });

        if (action === "attack" || action === "a") {
            await this.fight();
            difficulty += 1;
        } else if (action === "run" || action === "r") {
            await this.run();
        }
    }

    async run() {
        if (Math.floor(Math.random() * (this.player.speed + this.alien.speed)) < this.player.speed) {
            await printMessage("You escape successfully.");
        } else {
            await printMessage("You were too slow and the alien attacks you!");
            await this.alienAttack();
            if (this.player.hp <= 0){
                await gameOver();
            }
        }
        this.player.food -= 1;
        if (player.food <= 0){
            await printMessage("Not being able to find enough food, you starve and die in desperation.");
            await gameOver();
        }
    }

    async playerAttack() {
        this.alien.hp -= (this.player.currentWeapon.damage + this.player.attackPoints);
        await printMessage(this.player.currentWeapon.attackMessage);
    }

    async alienAttack() {
        this.player.hp -= (this.alien.weapon.damage + Math.floor(difficulty/2));
        await printMessage(this.alien.weapon.attackMessage);
    }
}
function saveToXML(player) {
    const xmlDoc = document.implementation.createDocument("", "", null);
    const root = xmlDoc.createElement("GameData");

    function createElement(name, value) {
        const element = xmlDoc.createElement(name);
        element.textContent = value;
        return element;
    }

    // Save Player Data
    const playerElement = xmlDoc.createElement("Player");
    playerElement.appendChild(createElement("HP", player.hp));
    playerElement.appendChild(createElement("AttackPoints", player.attackPoints));
    playerElement.appendChild(createElement("Speed", player.speed));
    playerElement.appendChild(createElement("Food", player.food));
    playerElement.appendChild(createElement("EnemiesKilled", player.enemiesKilled));
    playerElement.appendChild(createElement("Location", player.location));

    // Save Current Weapon
    const weaponElement = xmlDoc.createElement("CurrentWeapon");
    weaponElement.appendChild(createElement("Name", player.currentWeapon.name));
    playerElement.appendChild(weaponElement);

    // Save Inventory
    const inventoryElement = xmlDoc.createElement("Inventory");
    player.inventory.forEach(item => {
        const itemElement = xmlDoc.createElement("Item");
        itemElement.textContent = item.name;
        inventoryElement.appendChild(itemElement);
    });
    playerElement.appendChild(inventoryElement);
    root.appendChild(playerElement);

    // Save Map State
    const mapElement = xmlDoc.createElement("Map");

    // Save Empty Houses
    const emptyHousesElement = xmlDoc.createElement("EmptyHouses");
    map.emptyHouses.forEach(house => {
        const houseElement = xmlDoc.createElement("House");
        houseElement.textContent = house;
        emptyHousesElement.appendChild(houseElement);
    });
    mapElement.appendChild(emptyHousesElement);

    // Save Individual Houses & Emptied Rooms
    Object.keys(map).forEach(house => {
        if (house.startsWith("house")) {
            const houseElement = xmlDoc.createElement("House");
            houseElement.setAttribute("name", house);
            houseElement.appendChild(createElement("TimesEntered", map[house].timesEntered));

            const emptyRoomsElement = xmlDoc.createElement("EmptyRooms");
            map[house].emptyRooms.forEach(room => {
                const roomElement = xmlDoc.createElement("Room");
                roomElement.textContent = room;
                emptyRoomsElement.appendChild(roomElement);
            });

            // Save Rooms
            const roomsElement = xmlDoc.createElement("Rooms");
            Object.keys(map[house]).forEach(roomKey => {
                if (roomKey.startsWith("room")) {
                    const roomElement = xmlDoc.createElement("Room");
                    roomElement.setAttribute("number", roomKey.split(" ")[1]);
                    roomElement.setAttribute("type", map[house][roomKey].roomType);
                    roomsElement.appendChild(roomElement);
                }
            });
            houseElement.appendChild(roomsElement);

            houseElement.appendChild(emptyRoomsElement);
            mapElement.appendChild(houseElement);
        }
    });

    root.appendChild(mapElement);

    // Save Secrets Found
    const secretsElement = xmlDoc.createElement("SecretsFound");
    Object.keys(player.secretsFound).forEach(secret => {
        const secretElement = xmlDoc.createElement("Secret");
        secretElement.setAttribute("name", secret);
        secretElement.textContent = player.secretsFound[secret];
        secretsElement.appendChild(secretElement);
    });
    root.appendChild(secretsElement);

    // Save Game Progress
    const gameProgressElement = xmlDoc.createElement("GameProgress");
    gameProgressElement.appendChild(createElement("Day", day));
    gameProgressElement.appendChild(createElement("Difficulty", difficulty));
    gameProgressElement.appendChild(createElement("CurrentRoomCount", currentRoomCount));
    gameProgressElement.appendChild(createElement("MaxHP", player.maxhp));
    root.appendChild(gameProgressElement);

    xmlDoc.appendChild(root);

    // Convert XML to string and store in localStorage
    const serializer = new XMLSerializer();
    const xmlString = serializer.serializeToString(xmlDoc);
    localStorage.setItem("gameData", xmlString);

    console.log("Game saved successfully!");
}

function loadFromXML() {
    const xmlString = localStorage.getItem("gameData");
    if (!xmlString) {
        console.log("No saved game found.");
        return null;
    }

    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, "application/xml");

    // Load Player Data
    const playerElement = xmlDoc.querySelector("Player");
    const player = new Player(
        parseInt(playerElement.querySelector("HP").textContent),
        parseInt(playerElement.querySelector("AttackPoints").textContent),
        parseInt(playerElement.querySelector("Speed").textContent),
        parseInt(playerElement.querySelector("Food").textContent),
        playerElement.querySelector("Location").textContent
    );

    player.enemiesKilled = parseInt(playerElement.querySelector("EnemiesKilled").textContent);
    // Load Weapon
    const weaponName = playerElement.querySelector("CurrentWeapon Name").textContent;
    player.currentWeapon = WEAPONS[weaponName] || new Weapon(weaponName, "", 0, "", 1);
    
    // Load Inventory
    const inventoryItems = playerElement.querySelectorAll("Inventory Item");
    inventoryItems.forEach(itemNode => {
        const itemName = itemNode.textContent;
        if (ARTIFACTS[itemName]) {
            player.inventory.add(ARTIFACTS[itemName]);
        }else if(WEAPONS[itemName]){
            player.inventory.add(WEAPONS[itemName]);
        }
    });

    // Load Map State
    const mapElement = xmlDoc.querySelector("Map");
    map.emptyHouses = new Set();
    
    // Load Empty Houses
    mapElement.querySelectorAll("EmptyHouses House").forEach(houseNode => {
        map.emptyHouses.add(houseNode.textContent);
    });

    // Load Individual Houses & Emptied Rooms
    mapElement.querySelectorAll("House").forEach(houseElement => {
        const houseName = houseElement.getAttribute("name");
        map[houseName] = {
            emptyRooms: new Set(),
            timesEntered: 0
        };
        houseElement.querySelectorAll("Rooms Room").forEach(roomElement => {
            const roomNumber = `room ${roomElement.getAttribute("number")}`;
            const roomType = parseInt(roomElement.getAttribute("type"));
            map[houseName][roomNumber] = new Room(roomType);
        });

        houseElement.querySelectorAll("EmptyRooms Room").forEach(roomElement => {
            map[houseName].emptyRooms.add(roomElement.textContent);
        });
    });

    // Load Secrets Found
    const secretsElement = xmlDoc.querySelector("SecretsFound");
    secretsElement.querySelectorAll("Secret").forEach(secretNode => {
        const secretName = secretNode.getAttribute("name");
        player.secretsFound[secretName] = secretNode.textContent === "true";
    });

    // Load Game Progress
    const gameProgressElement = xmlDoc.querySelector("GameProgress");
    day = parseInt(gameProgressElement.querySelector("Day").textContent);
    difficulty = parseInt(gameProgressElement.querySelector("Difficulty").textContent);
    currentRoomCount = parseInt(gameProgressElement.querySelector("CurrentRoomCount").textContent);
    player.maxhp = parseInt(gameProgressElement.querySelector("MaxHP").textContent)

    console.log("Game loaded successfully!");
    return player;
}

async function clearXML() {
    const xmlDoc = document.implementation.createDocument("", "", null);
    const root = xmlDoc.createElement("GameData");

    function createElement(name, value) {
        const element = xmlDoc.createElement(name);
        element.textContent = value;
        return element;
    }

    // Reset Player Data
    const playerElement = xmlDoc.createElement("Player");
    playerElement.appendChild(createElement("HP", 100));
    playerElement.appendChild(createElement("AttackPoints", 5));
    playerElement.appendChild(createElement("Speed", 10));
    playerElement.appendChild(createElement("Food", 10));
    playerElement.appendChild(createElement("EnemiesKilled", 0));
    playerElement.appendChild(createElement("Location", "street"));

    // Reset Current Weapon
    const weaponElement = xmlDoc.createElement("CurrentWeapon");
    weaponElement.appendChild(createElement("Name", "Fists"));
    playerElement.appendChild(weaponElement);

    // Reset Inventory
    const inventoryElement = xmlDoc.createElement("Inventory");
    playerElement.appendChild(inventoryElement);
    root.appendChild(playerElement);

    // Reset Map State
    const mapElement = xmlDoc.createElement("Map");

    // Reset Empty Houses
    const emptyHousesElement = xmlDoc.createElement("EmptyHouses");
    mapElement.appendChild(emptyHousesElement);

    // Reset Individual Houses & Emptied Rooms
    for (let i = 1; i <= 10; i++) {
        const houseElement = xmlDoc.createElement("House");
        houseElement.setAttribute("name", `house ${i}`);
        houseElement.appendChild(createElement("TimesEntered", 0));

        const emptyRoomsElement = xmlDoc.createElement("EmptyRooms");
        houseElement.appendChild(emptyRoomsElement);

        const roomsElement = xmlDoc.createElement("Rooms");
        houseElement.appendChild(roomsElement);

        mapElement.appendChild(houseElement);
    }
    root.appendChild(mapElement);

    // Reset Secrets Found
    const secretsElement = xmlDoc.createElement("SecretsFound");
    ["The Orb of Time", "The Glove of Power", "Katana", "Dictionary"].forEach(secret => {
        const secretElement = xmlDoc.createElement("Secret");
        secretElement.setAttribute("name", secret);
        secretElement.textContent = false;
        secretsElement.appendChild(secretElement);
    });
    root.appendChild(secretsElement);

    // Reset Game Progress
    const gameProgressElement = xmlDoc.createElement("GameProgress");
    gameProgressElement.appendChild(createElement("Day", 1));
    gameProgressElement.appendChild(createElement("Difficulty", 1));
    gameProgressElement.appendChild(createElement("CurrentRoomCount", 0));
    gameProgressElement.appendChild(createElement("MaxHP", 100));
    root.appendChild(gameProgressElement);

    xmlDoc.appendChild(root);

    // Convert XML to string and store in localStorage
    const serializer = new XMLSerializer();
    const xmlString = serializer.serializeToString(xmlDoc);
    localStorage.setItem("gameData", xmlString);

    console.log("Game reset successfully!");
}

function createAlien() {
    const weaponKeys = Object.keys(ALIEN_WEAPONS);
    const weaponKey = weaponKeys[Math.floor(Math.random() * weaponKeys.length)];
    const weapon = ALIEN_WEAPONS[weaponKey];
    const name = ALIEN_NAMES[Math.floor(Math.random() * ALIEN_NAMES.length)];
    const hp = 20 + (difficulty * 10);
    const speed = 0 + (difficulty * 10);
    return new Alien(name, hp, weapon, speed);
}

async function gameOver() {
    printMessage("Game Over");
    printMessage(`You made it to day ${day}.`);
    sendHistoryGameResults(player);

    printMessage("Enter anything to start a new game");

    const getContinueChoice = async () => {
        const input = getInput();
        clearInput();
        return input;
    };

    const getContinueChoiceListener = () => {
        return new Promise(resolve => {
            const handleKeyPress = (event) => {
                if (event.key === "Enter" && !isEnterKeyPressed) {
                    isEnterKeyPressed = true;
                    resolve(getContinueChoice());
                    event.preventDefault();
                    document.removeEventListener("keydown", handleKeyPress);
                }
            };
    
            document.addEventListener("keydown", handleKeyPress);
        });
    };
    document.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            isEnterKeyPressed = false;
        }
    });

    await getContinueChoiceListener();

    endGame = false;
    await clearXML();
    window.location.reload();
}


async function sendHistoryGameResults() {

    try {
        //data parsing
        // let xmlData = localStorage.getItem("gameData");
        // const parser = new DOMParser();
        // const xmlDoc = parser.parseFromString(xmlData, "application/xml");
        // const gameProgressElement = xmlDoc.querySelector("GameProgress");
        // let day = parseInt(gameProgressElement.querySelector("Day").textContent);
        // let maxhp = parseInt(gameProgressElement.querySelector("MaxHP").textContent);
        // const playerElement = xmlDoc.querySelector("Player");
        // let enemiesKilled = parseInt(playerElement.querySelector("EnemiesKilled").textContent);

        //just relised we don't need data parsing here. all data are available as js variables
        //there's a minor delay in updating the xml, the js variable are always the newest
        //kept them just for you to check how to parse (more examples in loadFromXML())
        //if you implement save function, be sure to first call saveToXML(player)
        //before any data parsing and data sending starts

        let maxhp = player.maxhp;
        //day variable already available in js
        let enemiesKilled = player.enemiesKilled;

        let inv = [];
        for (let item of player.inventory){
            inv.push(item["name"]); 
        }
        //fetch stuff
        const response = await fetch('/gameApp/save_history/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/xml',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({
                "enemies_killed": enemiesKilled,
                "days_survived": day,
                "max_hp": maxhp,
                "inventory": inv
            }),
        });
        //wait for django view to response
        const data = await response.json();


        if (data.status === "success") {
            console.log("Game results saved successfully!");
        } else {
            console.error("Failed to save game results:", data.message);
        }
    } catch (error) {
        console.error("Error saving game results:", error);
    }
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function resetMap(player){
    map = { //reset the map first, otherwise it just executes katana and skips reset
        street: "street",
        emptyHouses: new Set(),
    };
    
    for (let i = 1; i <= 10; i++) {
        map[`house ${i}`] = { emptyRooms: new Set(), timesEntered: 0 };
    }

    if(!player.secretsFound["Katana"]){
        await printMessage("But first an old man approaches you");
        await printMessage("He appears to be holding an old sword");
        await printMessage('He walks up to you and he says "I don\'t really want this anymore..."');
        await printMessage("You want it? (yes/no)");

        const getSwordChoiceListener = () => {
            return new Promise(resolve => {
                const handleKeyPress = (event) => {
                    if (event.key === "Enter" && !isEnterKeyPressed) {
                        isEnterKeyPressed = true;
                        resolve(getSwordChoice());  // Resolve the sword choice
                        event.preventDefault();
                        document.removeEventListener("keydown", handleKeyPress); // Remove listener
                    }
                };
        
                document.addEventListener("keydown", handleKeyPress);
            });
        };
        
        document.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                isEnterKeyPressed = false;
            }
        });

        const getSwordChoice = async () => {
            const input = getInput().toLowerCase().trim();
            clearInput();
        
            if (!["yes", "no", "y", "n"].includes(input)) {
                await printMessage("Invalid input. Enter 'yes' or 'no'.");
                return await getSwordChoiceListener();
            }
        
            return input;
        };

        const swordChoice = await getSwordChoice();  // Wait for the sword choice before proceeding

        if (swordChoice === "yes" || swordChoice === "y") {
            await printMessage("He hands you the sword and walks into the sunset");
            player.currentWeapon = WEAPONS["Katana"];
            player.inventory.add(WEAPONS["Katana"]);
            await printMessage(`You now have ${WEAPONS["Katana"]}.`);
            saveToXML(player)
            player.secretsFound["Katana"] = true;
        } else {
            await printMessage("He crumbles to dust and blows away");
        }

        return 0
    }
}

async function play(player) {
    await printMessage("Enter 'q' to quit.")
    await printMessage("--------------------");
    await printMessage("You are in the street. You can enter any house numbered 1-10."); 

    const gameLoop = async () => {
        if (endGame) return;
        if (map["emptyHouses"].size == 10){
            await printMessage("You cleared every house in the neighborhood!");
            await printMessage("It's time to move on to the next one");
            await resetMap(player);
        }

        await printMessage("Which house would you like to enter? (1-10)");

        const getHouseChoice = async () => {
            const input = getInput();
            clearInput();

            if (input.toLowerCase() === "q") {
                endGame = true;
                return -1;
            }

            try {
                const houseNum = parseInt(input);
                if (houseNum == 0 && !player.secretsFound["Dictionary"]){
                    await printMessage("You found the secret house!");
                    await printMessage("It has a long pristine white hallway with a podium at the end");
                    await printMessage("You walk up to the podium and pick up the book on top");
                    player.inventory.add(ARTIFACTS["The Dictionary of the Ancients"]);
                    await printMessage(`You now have ${ARTIFACTS["The Dictionary of the Ancients"]}.`);
                    player.secretsFound["Dictionary"] = true;
                    return 0;
                }
                if (houseNum >= 1 && houseNum <= 10) {
                    return houseNum;
                } 
                else{
                    await printMessage("Invalid input. Enter a number between 1 and 10.");
                    return 0;
                }
            } catch (error) {
                await printMessage("Invalid input. Enter a number between 1 and 10.");
                return 0;
            }
        };

        let houseNum = 0;
        await new Promise(resolve => {
            const handleKeyPress = (event) => {
                if (event.key === "Enter" && !isEnterKeyPressed) {
                    isEnterKeyPressed = true;
                    getHouseChoice().then(num => {
                        houseNum = num;
                        resolve();
                    });
                    document.removeEventListener("keydown", handleKeyPress);
                }
            };

            document.addEventListener("keydown", handleKeyPress);
        });

        document.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                isEnterKeyPressed = false;
            }
        });

        if (endGame || houseNum === -1) {
            await gameOver();
            return;
        }

        if (houseNum > 0) {
            await player.move(houseNum);
            currentRoomCount += 1;

            if (currentRoomCount >= 8) { //fixed the bug where you refresh page when the following logic is not executed, room count just goes to infinity and do not increment day
                day += 1;
                player.food -= 1;
                difficulty += 1;
                currentRoomCount -= 8;
                await printMessage(`It is now day ${day}. You eat something, rest and gain 20 HP.`);
                player.hp += 20;
                player.maxHPUpdate();
                if (player.food <= 0){
                    await printMessage("Not being able to find enough food, you starve and die in desperation.");
                    await gameOver();
                }
            }
        }

        setTimeout(gameLoop, 500);
    };

    gameLoop();
}

const player = loadFromXML() || new Player(100, 5, 10, 10, map.street);
printMessage("Welcome to House Invader!");
play(player);