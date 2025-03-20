const MOCK_WEAPONS = [
    { name: "Sword", description: "A sharp blade.", damage: 10, attackMessage: "You slash the enemy.", rarity: 2 },
    { name: "Bow", description: "A ranged weapon.", damage: 8, attackMessage: "You shoot an arrow.", rarity: 1 },
    { name: "Axe", description: "A heavy weapon.", damage: 15, attackMessage: "You chop the enemy.", rarity: 3 },
];

const MOCK_ARTIFACTS = [
    { name: "Amulet of Power", description: "Increases your strength.", rarity: 4 },
    { name: "Ring of Speed", description: "Makes you faster.", rarity: 3 },
    { name: "Cloak of Invisibility", description: "Makes you invisible.", rarity: 5 },
    { name: "The Orb of Time", description: "Makes you sigma.", rarity: 5 },
    { name: "Shimschnar's Left Hand Glove", description: "Mysterious power.", rarity: 5 }
];

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

const ALIEN_NAMES = ["Zog", "Gorp", "Prip", "Geggin", "Nairn", "Hojjim", "Kada"];

let endGame = false;
let day = 1;
let difficulty = 1;
let currentRoomCount = 0;

const map = {
    street: "street",
    emptyHouses: new Set(),
};

for (let i = 1; i <= 10; i++) {
    map[`house ${i}`] = { emptyRooms: new Set(), timesEntered: 0 };
}

const messagesDiv = document.getElementById("messages");
const inputField = document.getElementById("input");
const submitButton = document.getElementById("submitButton");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function printMessage(message) {
    const messageElement = document.createElement("div");
    messageElement.className = "message";
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to the latest message

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
                const handleChoiceInput = () => {
                    resolve(getChoice());
                };

                submitButton.addEventListener("click", handleChoiceInput, { once: true });
                inputField.addEventListener("keypress", function(event) {
                    if (event.key === "Enter") {
                        submitButton.removeEventListener("click", handleChoiceInput);
                        resolve(getChoice());
                    }
                }, { once: true });
            });
        };

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
                            } else {
                                player.inventory.add(selectedItem);
                            }
                            await printMessage(`You now have ${selectedItem.name}.`);
                            player.food -= 1;
                            await printMessage("It cost you 1 Food.");
                        } else {
                            await printMessage("Invalid selection.");
                        }
                    } catch (error) {
                        await printMessage("Invalid selection.");
                    }
                };

                await new Promise(resolve => {
                    const handleItemInput = () => {
                        getItemChoice().then(resolve);
                    };

                    submitButton.addEventListener("click", handleItemInput, { once: true });
                    inputField.addEventListener("keypress", function(event) {
                        if (event.key === "Enter") {
                            submitButton.removeEventListener("click", handleItemInput);
                            getItemChoice().then(resolve);
                        }
                    }, { once: true });
                });
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
        this.attackPoints = attackPoints;
        this.currentWeapon = new Weapon("Fists", "Your fists", attackPoints, "You punch the alien.", 1);
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
            await this.exploreHouse(houseKey);
        }
    }

    async hasHouseBeenEntered(houseKey){
        check = false;
        
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
                const handleRoomInput = () => {
                    getRoomChoice().then(num => {
                        roomNum = num;
                        resolve();
                    });
                };

                submitButton.addEventListener("click", handleRoomInput, { once: true });
                inputField.addEventListener("keypress", function(event) {
                    if (event.key === "Enter") {
                        submitButton.removeEventListener("click", handleRoomInput);
                        getRoomChoice().then(num => {
                            roomNum = num;
                            resolve();
                        });
                    }
                }, { once: true });
            });
        }

        const roomKey = `room ${roomNum}`;

        await printMessage(`You enter room ${roomNum}.`);
        this.location = map[houseKey][roomKey];
        await this.location.searchRoom(this);

        if (!map[houseKey].emptyRooms.has(roomKey) && map[houseKey][roomKey].roomType == 0){
            map[houseKey].emptyRooms.add(roomKey);
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
            const handleLeaveInput = () => {
                resolve(getLeaveChoice());
            };

            submitButton.addEventListener("click", handleLeaveInput, { once: true });
            inputField.addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                submitButton.removeEventListener("click", handleLeaveInput);
                resolve(getLeaveChoice());
                }
            }, { once: true });
            });
        };

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
        this.player.attackPoints += 10;
        this.player.speed += 5;
        this.player.food += 2;
        this.player.enemiesKilled += 1;
        this.alien.hp = 0;

        if (Math.floor(Math.random() * 30) === 21 && !this.player.secretsFound["The Glove of Power"]) {
            await printMessage("You find a mysterious glove!");
            this.player.inventory.add(ARTIFACTS["Shimschnar's Left Hand Glove"]);
            await printMessage(`You now have ${ARTIFACTS["Shimschnar's Left Hand Glove"]}.`);
            this.player.secretsFound["The Glove of Power"] = true;
        }
    }

    async handleDefeat() {
        await printMessage("You have been defeated.");
        gameOver();
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
                const handleActionInput = () => {
                    getChoice().then(choice => {
                        action = choice;
                        resolve();
                    });
                };

                submitButton.addEventListener("click", handleActionInput, { once: true });
                inputField.addEventListener("keypress", function(event) {
                    if (event.key === "Enter") {
                        submitButton.removeEventListener("click", handleActionInput);
                        getChoice().then(choice => {
                            action = choice;
                            resolve();
                        });
                    }
                }, { once: true });
            });
        }

        if (action === "attack" || action === "a") {
            await this.fight();
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
        }
        this.player.food -= 1;
    }

    async playerAttack() {
        this.alien.hp -= this.player.currentWeapon.damage;
        await printMessage(this.player.currentWeapon.attackMessage);
    }

    async alienAttack() {
        this.player.hp -= this.alien.weapon.damage;
        await printMessage(this.alien.weapon.attackMessage);
    }
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

let userId = null;

async function fetchCurrentUser() {
    try {
        const response = await fetch('/play/api/current-user/');
        const data = await response.json();
        userId = data.user_id;
        console.log("Current user ID:", userId);
    } catch (error) {
        console.error("Error fetching current user:", error);
    }
}

// Fetch the user ID when the game starts
fetchCurrentUser();

// Example: Use the user ID to send game results
function gameOver() {
    printMessage("Game Over");
    printMessage(`Score: ${difficulty}`);
    printMessage(`You made it to day ${day}.`);

    if (userId) {
        // Send game results to Django
        sendGameResults(userId, player.enemiesKilled, day);
    } else {
        console.error("User ID not available.");
    }

    endGame = true;
}
async function sendGameResults(userId, enemiesKilled, daysSurvived) {
    try {
        const response = await fetch('/play/api/update-stats/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token for security
            },
            body: JSON.stringify({
                user_id: userId,
                enemies_killed: enemiesKilled,
                days_survived: daysSurvived,
            }),
        });

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

function resetMap(player){
    if(!player.secretsFound["Katana"]){
        printMessage("But first an old man approches you")
        printMessage("He appears to be holding an old sword")
        printMessage('He walks up to you and he says "I dont really want this anymore..."')
        printMessage("You want it? (yes/no)")
        const getSwordChoice = async () => {
            const input = getInput().toLowerCase().trim();
            clearInput();

            if (!["yes", "no", "y", "n"].includes(input)) {
                await printMessage("Invalid input. Enter 'yes' or 'no'.");
                return await getSwordChoiceListener();
            }

            return input;
        };

        const getSwordChoiceListener = () => {
            return new Promise(resolve => {
                const handleSwordInput = () => {
                    resolve(getSwordChoice());
                };

                submitButton.addEventListener("click", handleSwordInput, { once: true });
                inputField.addEventListener("keypress", function(event) {
                    if (event.key === "Enter") {
                        submitButton.removeEventListener("click", handleSwordInput);
                        resolve(getSwordChoice());
                    }
                }, { once: true });
            });
        };
        input = getSwordChoice();
        if (input == "yes" || input == "y"){
            printMessage("He hands you the sword and walks into the sunset")
            player.inventory.add(WEAPONS["Katana"]);
            printMessage(`You now have ${WEAPONS["Katana"]}.`);
        }
        else if (input == "no" || input == "n"){
            printMessage("He crumbles to dust and blows away")
        }
        player.secretsFound["Katana"] = true;
        return 0
    }
    const map = {
        street: "street",
        emptyHouses: new Set(),
    };
    
    for (let i = 1; i <= 10; i++) {
        map[`house ${i}`] = { emptyRooms: new Set(), timesEntered: 0 };
    }
}

async function play(player) {
    await printMessage("You are in the street. You can enter any house numbered 1-10. Enter 'q' to quit.");

    const gameLoop = async () => {
        if (endGame) return;
        if (map["emptyHouses"].size == 10){
            await printMessage("You cleared every house in the neighborhood!");
            await printMessage("It's time to move on to the next one");
            await resetMap(player);
        }

        await printMessage(player.toString());
        await printMessage(`Score: ${difficulty}`);
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
            const handleHouseInput = () => {
                getHouseChoice().then(num => {
                    houseNum = num;
                    resolve();
                });
            };

            submitButton.addEventListener("click", handleHouseInput, { once: true });
            inputField.addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                    submitButton.removeEventListener("click", handleHouseInput);
                    getHouseChoice().then(num => {
                        houseNum = num;
                        resolve();
                    });
                }
            }, { once: true });
        });

        if (endGame || houseNum === -1) {
            gameOver();
            return;
        }

        if (houseNum > 0) {
            await player.move(houseNum);
            currentRoomCount += 1;

            if (currentRoomCount === 5) {
                day += 1;
                difficulty += 1;
                currentRoomCount = 0;
                await printMessage(`It is now day ${day}. You rest and gain 20 HP.`);
                player.hp += 20;
            }
        }

        setTimeout(gameLoop, 500);
    };

    gameLoop();
}

const player = new Player(100, 5, 10, 10, map.street);
printMessage("Welcome to Alien Survival Game!");
play(player);