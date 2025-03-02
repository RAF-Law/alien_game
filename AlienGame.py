import random
from abc import ABC, abstractmethod
import time

class Alien(ABC):
    def __init__(self, name, hp, weapon, speed):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.speed = speed

class Boss(Alien):
    def __init__(self, name, hp, weapon, speed):
        super().__init__(name, hp, weapon, speed)
        self.type = "boss"

class Minion(Alien):
    def __init__(self, name, hp, weapon, speed):
        super().__init__(name, hp, weapon, speed)
        self.type = "minion"

rarities = {1 : "Common", 2 : "Uncommon", 3 : "Rare", 4 : "Epic", 5 : "Legendary"}

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

class House: 
    def __init__(self):
        self.loot = []
        
    def generateLoot(self):
        rarityCap = random.randint(2, 5)
        lootNum = random.randint(0, 2)
        i=0
        while i<= lootNum:
            newWep = random.choice(list(weapons.values()))
            if newWep not in self.loot and newWep.rarity <= rarityCap:
                self.loot.append(newWep)
                i+=1

    def houseSearch(self):
        self.generateLoot()
        print("You search the house and find:")
        time.sleep(2)
        for index, weapon in enumerate(self.loot):
            print(str(index + 1) + ": A " + weapon.name + " - " + weapon.description + " | " + rarities[weapon.rarity] + " |")
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
                    time.sleep(2)
                except IndexError:
                    print("Invalid input, enter the number associated with the weapon you want to take")
        elif choice.lower() == "q":
            end = True
        else:
            print("You leave the weapon(s) behind")
            time.sleep(2)

class Player:
    def __init__(self, HP, attackPoints, speed, food, location):
        self.HP = HP
        self.currentWeapon = Weapon("Fists", "Your fists", attackPoints, "You punch the alien", 1)
        self.speed = speed
        self.food = food
        self.location = location
    
    def move (self, x, y, prevx, prevy):
        self.location = mapGrid[x][y]
        if self.location == "s":
            print("You are in the street")
            time.sleep(2)
            
        elif self.location == "h":
            print("You enter a house")
            time.sleep(2)
            house = House()
            house.houseSearch()
            mapGrid[x][y] = "eh"
            xpos, ypos = prevx, prevy
            print("You are back in the street")

        elif self.location == "eh":
            print("You enter a house")
            time.sleep(1)
            print("It is empty")
            time.sleep(1)
            xpos, ypos = prevx, prevy
            print("You are back in the street")
            time.sleep(2)

        elif self.location == "a":
            alien = createAlien()
            time.sleep(2)
            battle = Battle(self, alien)
            battle.encounter(prevx, prevy)

        elif self.location == "bh":
            print("You enter the boss's house")

class Battle():
    def __init__(self, player, alien):
        self.player = player
        self.alien = alien
        self.turn = 0

    def fight(self):
        totalSpeed = self.player.speed + self.alien.speed
        while self.player.HP > 0 and self.alien.hp > 0:
            speedVal = random.randint(1, totalSpeed)
            if speedVal <= self.player.speed:
                self.playerAttack()
            else:
                self.alienAttack()

    def encounter(self, prevx, prevy):
        print("You encounter a " + self.alien.type + " alien. It says it's name is " + self.alien.name)
        time.sleep(2)
        print(self.alien.name + " has a " + self.alien.weapon.name + " | " + rarities[self.alien.weapon.rarity] + " |")
        time.sleep(2)
        print("What would you like to do?, you can attack or run")
        action = input()
        if action.lower() == "attack":
            self.fight()   
            difficulty += 1
            mapGrid[xpos][ypos] = "s"
        elif action.lower() == "run":
            print("You run away")
            xpos, ypos = prevx, prevy
            player.location = mapGrid[xpos][ypos]
            time.sleep(2)
            
    def playerAttack(self):
        self.alien.hp -= self.player.currentWeapon.damage
        print(self.player.currentWeapon.attackMessage)
        time.sleep(2)

    def alienAttack(self):
        self.player.HP -= self.alien.weapon.damage
        print("The alien attacks you with it's " + self.alien.weapon.name)
        time.sleep(2)


locations = {"s" : "street", "h" : "house", "a" : "alien", "bh" : "boss house", "eh" : "empty house"}

rarities = {1 : "Common", 2 : "Uncommon", 3 : "Rare", 4 : "Epic", 5 : "Legendary"}

weapons = {"Ak-47" : Weapon("Ak-47", "A powerful assault Rifle", 40, "You shoot the alien with your Ak-47", 3),
           "Glock" : Weapon("Glock", "A semi-automatic pistol", 20, "You shoot the alien with your Glock", 2),
           "Baseball Bat" : Weapon("Baseball Bat", "A wooden baseball bat with barbed wire wrapped around it", 15, "You hit the alien with your gruesome baseball bat", 2),
           "MAC-10" : Weapon("MAC-10", "A submachine gun with a high fire rate", 30, "You spray the alien with your MAC-10", 3),
           "Machete" : Weapon("Machete", "A terrifying blade with a serrated edge", 25, "You slice the alien with your machete", 2),
           "Laser Gun" : Weapon("Laser Gun", "A futuristic laser weapon not of this world", 50, "You zap the alien with your Laser Gun", 4),
           "Plasma Rifle" : Weapon("Plasma Rifle", "A high-tech energy charged rifle", 60, "You blast the alien with your Plasma Rifle", 4),
           "Energy Sword" : Weapon("Energy Sword", "A sword made of pure energy that emits a loud hum", 75, "You slash the alien with your Energy Sword", 5),
           "Flamethrower" : Weapon("Flamethrower", "A weapon that shoots flames, incinerating enemies", 55, "You burn the alien with your Flamethrower", 4),
           "Railgun" : Weapon("Railgun", "A powerful electromagnetic weapon that can fire from up to 65 kilometres away", 90, "You blow a hole through the alien with your Railgun", 5),
           "Katana" : Weapon("影の龍", "A katana that was passed down through many generations of honorable samurai", 100, "You slice through the alien with unheavenly precision", 5),
           "Knife" : Weapon("Knife", "A sharp knife", 10, "You stab the alien with your knife", 1),
           "Tazer" : Weapon("Tazer", "A tazer that can electricute enemies", 8, "You taze the alien", 1),
           "Chicken" : Weapon("Chicken", "A chicken that attacks aliens for some reason", 5, "You throw the chicken at the alien", 1),
           "Tea and Biscuits" : Weapon("Tea and Biscuits", "A cup of tea and some biscuits", 3, "You throw hot tea and a couple of biscuits at the alien", 1),
           "Crowbar" : Weapon("Crowbar", "An old, rusty crowbar", 15, "You hit the alien with your crowbar", 2),
           "Revolver" : Weapon("Revolver", "A six-shooter revolver", 25, "You shoot the alien with your revolver", 2),
           "Sniper Rifle" : Weapon("Sniper Rifle", "A high-powered sniper rifle", 60, "You snipe the alien with your sniper rifle", 4),
           "Rocket Launcher" : Weapon("Rocket Launcher", "A weapon that fires explosive rockets", 70, "You blow the alien up with your rocket launcher", 4),
           "Grenade" : Weapon("Grenade", "A grenade that explodes on impact", 50, "You throw the grenade at the alien", 3),
           "Shotgun" : Weapon("Shotgun", "A shotgun that fires a spread of pellets", 45, "You blast the alien with your shotgun", 3),
           "Little Monster" : Weapon("Little Monster", "A small, mysterious creature that really hates aliens", 35, "You throw your little monster at the alien", 1),
           }

artifacts = {}
#      W
#   S<-+->N
#      E
mapGrid = [
["a", "a", "h", "h", "bh", "s"],
["s", "s", "s", "s", "a", "h"],
["a", "s", "h", "h", "h", "s"],
["s", "s", "s", "s", "a", "h"],
["a", "s", "a", "a", "s", "h"],
["s", "h", "h", "bh", "h", "s"]
]

minionWeapons = []

def createAlien():
    if player.location == "a":
        return Minion("Minion", 50, random.choice(list(weapons.values())), 10)
    elif player.location == "bh":
        return Boss("Boss", 100, random.choice(list(weapons.values())), 20)

def play():
    print(mapGrid[2])
    global difficulty
    difficulty = 1
    global end 
    end = False
    global xpos 
    xpos = 2
    global ypos 
    ypos = 1
    global player 
    player = Player(100, 5, 10, 10, mapGrid[xpos][ypos])
    print("You are in the street. You can move North, South, East, or West. Enter 'q' to quit at any stage")
    time.sleep(4)
    print("Your current weapon is " + player.currentWeapon.toString())
    time.sleep(2)
    while end == False:
        direction = input()
        if direction.lower() == "north":
            if ypos!=5:
                player.move(xpos, ypos+1, xpos, ypos)
                if player.location != "h" and player.location != "bh" and player.location != "eh" and player.location != "a":
                    ypos += 1
                    player.location = mapGrid[xpos][ypos]
                else:
                    player.location = mapGrid[xpos][ypos]
            else:
                print("You can't move there")
        elif direction.lower() == "south":
            if ypos!=0:
                player.move(xpos, ypos-1, xpos, ypos)
                if player.location != "h" and player.location != "bh" and player.location != "eh" and player.location != "a":
                    ypos -= 1
                    player.location = mapGrid[xpos][ypos]
                else:
                    player.location = mapGrid[xpos][ypos]
            else:
                print("You can't move there")
        elif direction.lower() == "east":
            if xpos!=5:
                player.move(xpos + 1, ypos, xpos, ypos)
                if player.location != "h" and player.location != "bh" and player.location != "eh" and player.location != "a":
                    xpos += 1
                    player.location = mapGrid[xpos][ypos]
                else:
                    player.location = mapGrid[xpos][ypos]
            else:
                print("You can't move there")
        elif direction.lower() == "west":
            if xpos!=0:
                player.move(xpos - 1, ypos, xpos, ypos)
                if player.location != "h" and player.location != "bh" and player.location != "eh" and player.location != "a":
                    xpos -= 1
                    player.location = mapGrid[xpos][ypos]
                else:
                    player.location = mapGrid[xpos][ypos]
            else:
                print("You can't move there")
        elif direction.lower() == "q":
            end = True
        else:
            print("Invalid input, please enter North, South, East, or West")

    print("Game over")
    time.sleep(2)
    exit()

play()