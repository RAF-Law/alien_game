import random
from abc import ABC, abstractmethod
import time

rarities = {1 : "Common", 2 : "Uncommon", 3 : "Rare", 4 : "Epic", 5 : "Legendary"}

class Alien():
    def __init__(self, name, hp, weapon, speed):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.speed = speed

class Weapon:
    def __init__(self, name, description, damage, attackMessage, rarity):
        self.name = name
        self.description = description
        self.damage = damage
        self.attackMessage = attackMessage
        self.rarity = rarity
    
    def showAttackMessage(self):
        print(self.attackMessage)

    def toString(self):
        return self.name + " - " + self.description + " (" + str(self.damage) + " damage)" + " | " + rarities[self.rarity] + " |"

class Room: 
    def __init__(self):
        self.loot = []
        
    def generateWeaponLoot(self):
        rarityCap = random.randint(1, 3)
        lootNum = random.randint(0, 2)
        i=0
        while i<= lootNum:
            newWep = random.choice(list(weapons.values()))
            if newWep not in self.loot and newWep.rarity <= rarityCap:
                self.loot.append(newWep)
                i+=1

    def generateArtifactLoot(self):
        rarityCap = random.randint(1, 3)
        lootNum = random.randint(0, 2)
        i=0
        while i<= lootNum:
            newArt = random.choice(list(artifacts.values()))
            if newArt not in self.loot and newArt.rarity <= rarityCap:
                self.loot.append(newArt)
                i+=1

    def artifactRoomSearch(self):
        self.generateArtifactLoot()
        print("You find yourself in an room filled with strange artifacts")
        time.sleep(2)
        print("You search the room and find:")
        time.sleep(2)
        for index, artifact in enumerate(self.loot):
            print(str(index + 1) + ": A " + artifact.name + " - " + artifact.description + " | " + rarities[artifact.rarity] + " |")
            time.sleep(1)
        print("Would you like to take any of these artifacts?")
        choice = input()
        while choice.lower() != "yes" and choice.lower() != "no" and choice.lower() != "q":
            print("Invalid input, enter 'yes' or 'no'")
            choice = input()
        if choice.lower() == "yes":
            print("Which artifact would you like to take?")
            artifactChoice = int(input())
            validCheck = False
            while validCheck == False:
                try:
                    player.inventory.append(self.loot[artifactChoice - 1])
                    print("You now have a " + self.loot[artifactChoice - 1].name)
                    time.sleep(2)
                    self.loot[artifactChoice -1].toString()
                    validCheck = True
                    print("It cost you 1 Food")
                    player.food -= 1
                    time.sleep(2)
                except IndexError:
                    print("Invalid input, enter the number associated with the artifact you want to take")
        elif choice.lower() == "q":
            global end
            end = True
        else:
            print("You leave the artifact(s) behind")
            time.sleep(2)

    def weaponRoomSearch(self):
        self.generateWeaponLoot()
        print("You find yourself in a room filled with weapons")
        time.sleep(2)
        print("You search the room and find:")
        time.sleep(2)
        for index, weapon in enumerate(self.loot):
            print(str(index + 1) + ": A " + weapon.name +  " | " + rarities[weapon.rarity] + " |")
            time.sleep(1)
        print("Would you like to take any of these weapons?")
        choice = input()
        while choice.lower() != "yes" and choice.lower() != "no" and choice.lower() != "q":
            print("Invalid input, enter 'yes' or 'no'")
            choice = input()
        if choice.lower() == "yes":
            print("Which weapon would you like to take?")
            weaponChoice = int(input())
            validCheck = False
            while validCheck == False:
                try:
                    player.currentWeapon = self.loot[int(weaponChoice) - 1]
                    print("You now have a " + player.currentWeapon.name)
                    time.sleep(2)
                    print(player.currentWeapon.toString())
                    validCheck = True
                    print("It cost you 1 Food")
                    player.food -= 1
                    time.sleep(2)
                except IndexError:
                    print("Invalid input, enter the number associated with the weapon you want to take")
        elif choice.lower() == "q":
            end = True
        else:
            print("You leave the weapon(s) behind")
            time.sleep(2)

class Player:
    def __init__(self, hp, attackPoints, speed, food, location):
        self.hp = hp
        self.attackPoints = attackPoints
        self.currentWeapon = Weapon("Fists", "Your fists", attackPoints, "You punch the alien", 1)
        self.inventory = []
        self.speed = speed
        self.food = food
        self.location = location
        self.enemied_killed = 0

    def move(self, house):
        houseStr = "house " + str(house)
        numOfRooms = random.randint(2, 6)
        for i in range(1, numOfRooms + 1):
            roomStr = "room " + str(i)
            map[houseStr][roomStr] = Room()
        print("You enter " + houseStr + ". There are " + str(numOfRooms) + " rooms in this house. Which room would you like to enter?")
        roomNum = int(input())
        while roomNum <= 0 or roomNum > numOfRooms:
            print("Invalid input, please enter a number 1-" + str(numOfRooms))
            roomNum = int(input())
        roomStr = "room " + str(roomNum)            
        self.location = map[houseStr][roomStr]
        global leave
        leave = False
        while leave == False:
            roomStr = "room " + str(roomNum) 
            roomType = random.randint(1, 3)
            if roomStr in map[houseStr]["empty"]:
                roomType = 0
            match roomType:
                case 0:
                    print("This room is empty")
                case 1:
                    map[houseStr][roomStr].weaponRoomSearch()
                case 2:
                    map[houseStr][roomStr].artifactRoomSearch()
                case 3:
                    alien = createAlien()
                    battle = Battle(player, alien)
                    battle.encounter()

            if len(map[houseStr]) == len(map[houseStr]["empty"]):
                print("You have emptied all rooms in this house")
                leave = True
            if leave == False:
                print("Would you like to leave the house?")
                leaveChoice = input()
                leave = bool(leaveChoice)
                if roomStr not in map[houseStr]["empty"]:
                    map[houseStr]["empty"].append(roomStr)
                if leaveChoice.lower() == "yes":
                    leave = True
                else:
                    leave = False
            while leave == False and leaveChoice.lower() != "yes" and leaveChoice.lower() != "no":
                print("Invalid input, enter 'yes' or 'no'")
                leaveChoice = input()
                if leaveChoice.lower() == "yes":
                    leave = True
                else:
                    leave = False
            if leave==False:
                print("Which room would you like to enter next?")
                roomNum = int(input())
                while roomNum <= 0 or roomNum > numOfRooms:
                    print("Invalid input, please enter a number 1-" + str(numOfRooms))
                    roomNum = int(input())
            else:
                print("You leave the house")
                player.location = map["street"]
                time.sleep(2)
            update()
    
    def toString(self):
        return "HP: " + str(self.hp) + " | Attack Points: " + str(self.attackPoints) + " | Speed: " + str(self.speed) + " | Food: " + str(self.food)

class Artifact:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity    

    def toString(self):
        return self.name + " - " + self.description + " | " + rarities[self.rarity] + " |"


class Battle():
    def __init__(self, player, alien):
        self.player = player
        self.alien = alien
        self.turn = 0

    def fight(self):
        totalSpeed = self.player.speed + self.alien.speed
        while self.player.hp > 0 and self.alien.hp > 0:
            speedVal = random.randint(1, totalSpeed)
            if speedVal <= self.player.speed:
                self.playerAttack()
                if self.alien.hp > 0:
                    self.alienAttack()
                else:
                    self.alien.hp = 0
                    print("You steal " + self.alien.name + "'s lunch | +4 Food")
                    self.player.food += 4
            else:
                self.alienAttack()
                if self.player.hp > 0:
                    self.playerAttack()
                else:
                    self.player.hp = 0
            print("You: " + self.player.hp)
            print(self.alien.name + ": " + self.alien.hp)
        if self.alien.hp<=0:
            print("You killed " + self.alien.name)
            self.player.hp += 20
            self.player.attackPoints += 10
            self.player.speed += 5
            print("You gain some of " + self.alien.name + "'s life force | +20 HP | +10 attack points | +5 speed |")
            self.player.food += 2
            print("You also steal " + self.alien.name + "'s lunch | +2 Food |")
            self.player.enemies_killed += 1
        if self.player.hp<=0:
            gameOver()

    def encounter(self):
        print("You encounter an alien. It says it's name is " + self.alien.name)
        time.sleep(2)
        print(self.alien.name + " has a " + self.alien.weapon.name + " | " + rarities[self.alien.weapon.rarity] + " |")
        time.sleep(2)
        print("What would you like to do?, you can attack or run")
        action = input()
        if action.lower() == "attack":
            self.fight()  
            global difficulty 
            difficulty += 1
        elif action.lower() == "run":
            print("You run away")
            totalSpeed = self.player.speed + self.alien.speed
            speedVal = random.randint(1, totalSpeed)
            if speedVal <= self.player.speed:
                print("You escape")
                time.sleep(2)
            else:
                print("You were too slow and the alien attacks you before you can escape")
                self.alienAttack()
            time.sleep(2)
            player.food -= 1
            global leave
            leave = True
            
    def playerAttack(self):
        self.alien.hp -= self.player.currentWeapon.damage
        print(self.player.currentWeapon.attackMessage)
        time.sleep(2)

    def alienAttack(self):
        self.player.hp -= self.alien.weapon.damage
        print(self.alien.weapon.attackMessage)
        time.sleep(2)

rarities = {1 : "Common", 2 : "Rare", 3 : "Legendary", 4 : "Secret"}

weapons = {"Ak-47" : Weapon("Ak-47", "A powerful assault Rifle", 40, "You shoot the alien with your Ak-47", 2),
           "Baseball Bat" : Weapon("Baseball Bat", "A wooden baseball bat with barbed wire wrapped around it", 15, "You hit the alien with your gruesome baseball bat", 1),
           "Laser Gun" : Weapon("Laser Gun", "A futuristic laser weapon not of this world", 50, "You zap the alien with your Laser Gun", 2),
           "Plasma Rifle" : Weapon("Plasma Rifle", "A high-tech energy charged rifle", 60, "You blast the alien with your Plasma Rifle", 3),
           "Energy Sword" : Weapon("Energy Sword", "A sword made of pure energy that emits a loud hum", 75, "You slash the alien with your Energy Sword", 3),
           "Flamethrower" : Weapon("Flamethrower", "A weapon that shoots flames, incinerating enemies", 55, "You burn the alien with your Flamethrower", 2),
           "Railgun" : Weapon("Railgun", "A powerful electromagnetic weapon that can fire from up to 65 kilometres away", 90, "You blow a hole through the alien with your Railgun", 3),
           "Katana" : Weapon("影の龍", "A katana that was passed down through many generations of honorable samurai", 100, "You slice through the alien with unheavenly precision", 4),
           "Chicken" : Weapon("Chicken", "A chicken that attacks aliens for some reason", 10, "You throw the chicken at the alien", 1),
           "Revolver" : Weapon("Revolver", "A six-shooter revolver", 25, "You shoot the alien with your revolver", 1),
           "Shotgun" : Weapon("Shotgun", "A shotgun that fires a spread of pellets", 45, "You blast the alien with your shotgun", 2),
           }

artifacts = {
    "Cosmic Crystal" : Artifact("Cosmic Crystal", "A crystal that glows with an otherworldly light", 3),
    "Galactic Map" : Artifact("Galactic Map", "A map showing the locations of alien worlds", 2),
    "Alien Artifact" : Artifact("Alien Artifact", "An artifact of unknown origin and purpose", 1),
    "Extraterrestrial Coin" : Artifact("Extraterrestrial Coin", "A coin from an alien currency", 1),
    "Space Helmet" : Artifact("Space Helmet", "A helmet worn by an alien astronaut", 2),
    "Alien Skull" : Artifact("Alien Skull", "The skull of a long-dead alien", 3),
    "Stardust" : Artifact("Stardust", "A handful of glowing stardust", 1),
    "Meteorite Fragment" : Artifact("Meteorite Fragment", "A fragment of a meteorite", 2),
    "Alien Fossil" : Artifact("Alien Fossil", "A fossilized alien creature", 3),
    "Space Gem" : Artifact("Space Gem", "A gem from outer space", 2),
    "Alien Egg" : Artifact("Alien Egg", "An egg containing an alien lifeform", 1),
    "Cosmic Dust" : Artifact("Cosmic Dust", "A small amount of cosmic dust", 1),
    "Alien Amulet" : Artifact("Alien Amulet", "An amulet with alien symbols", 2),
    "Galactic Artifact" : Artifact("Galactic Artifact", "An artifact from another galaxy", 3),
    "Space Relic" : Artifact("Space Relic", "A relic from outer space", 2),
    "Alien Crystal" : Artifact("Alien Crystal", "A crystal with alien properties", 3),
    "Extraterrestrial Relic" : Artifact("Extraterrestrial Relic", "A relic from an extraterrestrial civilization", 2),
    "Shimschnar's Left Hand Glove" : Artifact("Shimschnar's Left Hand Glove", "The left hand glove of the legendary alien warrior Shimschnar, it's true ability is unknown", 4),
    "The Dictionary of the Ancients" : Artifact("The Dictionary of the Ancients", "A book containing the language of an ancient alien civilization", 4),
    "The Orb of Time" : Artifact("The Orb of Time", "An orb that can manipulate time itself, but you have no idea how it works", 4)
}

#Rooms will be generated inside each house
map = {"street" : "street", 
"EmptyHouses" : [],
"house 1" : {"empty" : []},
"house 2" : {"empty" : []},
"house 3" : {"empty" : []},
"house 4" : {"empty" : []},
"house 5" : {"empty" : []},
"house 6" : {"empty" : []},
"house 7" : {"empty" : []},
"house 8" : {"empty" : []},
"house 9" : {"empty" : []},
"house 10" : {"empty" : []}
}

def update():
    global player
    global day
    global cur_room_count
    global difficulty
    global alienWeapons
    alienWeapons = {"goppin" : Weapon("Goppin", "A weapon that fires a stream of plasma", 5+(difficulty*5), "The alien shoots you with a stream of plasma", 1),
    "Sponk" : Weapon("Sponk", "A weapon that fires a burst of energy", 15+(difficulty*5), "The alien blasts you with a burst of energy", 2),
    "Zorblax" : Weapon("Zorblax", "A weapon that shoots a beam of energy", 25+(difficulty*5), "The alien fires a beam of energy at you", 3),}
    cur_room_count += 1
    if cur_room_count == 5:
        day += 1
        #print("You go to sleep")
        #time.sleep(2)
        print("It is now day " + day)
        difficulty += 1
        #player.food -= 3

alienNames = ["Zog", "Gorp", "Prip", "Geggin", "Nairn", "Hojjim", "Kada"]

def gameOver():
    print("Game Over")
    time.sleep(1)
    print("Score: " + str(difficulty))
    print("You made it to day " + str(day))
    time.sleep(2)
    exit()


def createAlien():
    weapon = random.choice(list(alienWeapons.values()))
    name = random.choice(alienNames)
    hp = 20 + (difficulty*10)
    speed = 0 + (difficulty*10)
    alien = Alien(name, hp, weapon, speed)
    return alien


def play():
    global cur_room_count
    cur_room_count = 0
    global day
    day = 1
    global difficulty
    difficulty = 1
    global end 
    end = False
    global player 
    player = Player(100, 5, 10, 10, map["street"])
    print("You are in the street. You can enter any house numbered 1-10. enter 'q' to quit")
    time.sleep(4)
    print("Your current weapon is " + player.currentWeapon.toString())
    time.sleep(2)
    while end == False:
        print(player.toString())
        print("Score: " + str(difficulty))
        houseNum = input("Which house would you like to enter? ")
        if houseNum.lower() == "q":
            end = True
            break
        if int(houseNum) <= 10 or int(houseNum) >0:
            houseNum = int(houseNum)
            player.move(houseNum)
        else:
            print("Invalid input, please enter a number 1-10")
    gameOver()

play()