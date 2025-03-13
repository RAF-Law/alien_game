import random
import time
from gameApp.models import Weapon as WeaponModel, Artifact as ArtifactModel

class Alien:
    def __init__(self, name, hp, weapon, speed):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.speed = speed

class Weapon:
    def __init__(self, name, description, damage, attack_message, rarity):
        self.name = name
        self.description = description
        self.damage = damage
        self.attack_message = attack_message
        self.rarity = rarity

    def show_attack_message(self):
        print_message(self.attack_message)

    def __str__(self):
        return f"{self.name} - {self.description} ({self.damage} damage) | {RARITIES[self.rarity]} |"

class Artifact:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} - {self.description} | {RARITIES[self.rarity]} |"

def fetch_weapons():
    weapons = {}
    for weapon in WeaponModel.objects.all():
        weapons[weapon.name] = Weapon(
            name=weapon.name,
            description=weapon.description,
            damage=weapon.damage,
            attack_message=weapon.attack_message,
            rarity=weapon.rarity
        )
    return weapons

def fetch_artifacts():
    artifacts = {}
    for artifact in ArtifactModel.objects.all():
        artifacts[artifact.name] = Artifact(
            name=artifact.name,
            description=artifact.description,
            rarity=artifact.rarity
        )
    return artifacts

RARITIES = {1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic", 5: "Legendary"}

ALIEN_WEAPONS = {
    "Goppin": Weapon("Goppin", "A weapon that fires plasma.", 5, "The alien shoots you with plasma.", 1),
    "Sponk": Weapon("Sponk", "A weapon that fires energy bursts.", 15, "The alien blasts you with energy.", 2),
    "Zorblax": Weapon("Zorblax", "A weapon that shoots energy beams.", 25, "The alien fires a beam at you.", 3),
}

ALIEN_NAMES = ["Zog", "Gorp", "Prip", "Geggin", "Nairn", "Hojjim", "Kada"]

END_GAME = False
FOUND_GLOVE = False
REPEAT_SECRET = False

DAY = 1
DIFFICULTY = 1
CURRENT_ROOM_COUNT = 0

WEAPONS = fetch_weapons()
ARTIFACTS = fetch_artifacts()

MAP = {
    "street": "street",
    "empty_houses": [],
    **{f"house {i}": {"empty_rooms": [], "times_entered": 0} for i in range(1, 11)},
}

def print_message(message):
    print(message)

def get_input():
    return input().strip()

class Room:
    def __init__(self, room_type, alien=None):
        self.loot = []
        self.room_type = room_type
        self.alien = alien

    def generate_loot(self, items, rarity_cap):
        loot_num = random.randint(0, 2)
        for _ in range(loot_num):
            item = random.choice(list(items.values()))
            if item.rarity <= rarity_cap and item not in self.loot:
                self.loot.append(item)

    def search_room(self, player):
        if self.room_type == 0:
            print_message("This room is empty.")
        elif self.room_type == 1:
            self.generate_loot(WEAPONS, random.randint(1, 3))
            self.handle_loot(player, "weapon")
        elif self.room_type == 2:
            self.generate_loot(ARTIFACTS, random.randint(1, 3))
            self.handle_loot(player, "artifact")
        elif self.room_type == 3:
            if self.alien is None:
                self.alien = create_alien()
            Battle(player, self.alien).encounter()

    def handle_loot(self, player, loot_type):
        print_message(f"You find yourself in a room filled with {loot_type}s.")
        time.sleep(2)
        print_message("You search the room and find:")
        time.sleep(2)
        for index, item in enumerate(self.loot):
            print_message(f"{index + 1}: {item}")
            time.sleep(1)
        print_message("Would you like to take any of these items? (yes/no)")
        choice = get_input().lower()
        while choice not in ["yes", "no", "q"]:
            print_message("Invalid input. Enter 'yes', 'no', or 'q' to quit.")
            choice = get_input().lower()
        if choice == "yes":
            print_message(f"Which {loot_type} would you like to take?")
            try:
                item_choice = int(get_input()) - 1
                selected_item = self.loot[item_choice]
                if loot_type == "weapon":
                    player.current_weapon = selected_item
                else:
                    player.inventory.append(selected_item)
                print_message(f"You now have {selected_item.name}.")
                player.food -= 1
                print_message("It cost you 1 Food.")
            except (IndexError, ValueError):
                print_message("Invalid selection.")
        elif choice == "q":
            global END_GAME
            END_GAME = True
        else:
            print_message(f"You leave the {loot_type}(s) behind.")

class Player:
    def __init__(self, hp, attack_points, speed, food, location):
        self.hp = hp
        self.attack_points = attack_points
        self.current_weapon = Weapon("Fists", "Your fists", attack_points, "You punch the alien.", 1)
        self.inventory = []
        self.speed = speed
        self.food = food
        self.location = location
        self.enemies_killed = 0

    def __str__(self):
        return f"HP: {self.hp} | Attack Points: {self.attack_points} | Speed: {self.speed} | Food: {self.food}"

    def move(self, house):
        house_key = f"house {house}"
        if house_key in MAP["empty_houses"]:
            print_message("This house is empty.")
            return
        MAP[house_key]["times_entered"] += 1
        if MAP[house_key]["times_entered"] == 5 and not REPEAT_SECRET:
            print_message("You have spent so much time in this house that you find a hidden artifact!")
            time.sleep(2)
            player.inventory.append(ARTIFACTS["The Orb of Time"])
            print_message(f"You now have {ARTIFACTS['The Orb of Time']}.")
            REPEAT_SECRET = True
        else:
            print_message(f"You enter {house_key}.")
            self.explore_house(house_key)

    def explore_house(self, house_key):
        num_rooms = random.randint(2, 6)
        for i in range(1, num_rooms + 1):
            room_key = f"room {i}"
            room_type = random.randint(0, 3)
            MAP[house_key][room_key] = Room(room_type)
        print_message(f"There are {num_rooms} rooms in this house. Which room would you like to enter?")
        room_num = int(get_input())
        while room_num < 1 or room_num > num_rooms:
            print_message(f"Invalid input. Enter a number between 1 and {num_rooms}.")
            room_num = int(get_input())
        room_key = f"room {room_num}"
        self.location = MAP[house_key][room_key]
        self.location.search_room(self)
        if room_key not in MAP[house_key]["empty_rooms"]:
            MAP[house_key]["empty_rooms"].append(room_key)
        if len(MAP[house_key]["empty_rooms"]) == num_rooms:
            print_message("You have emptied all rooms in this house.")
            MAP["empty_houses"].append(house_key)

class Battle:
    def __init__(self, player, alien):
        self.player = player
        self.alien = alien

    def fight(self):
        while self.player.hp > 0 and self.alien.hp > 0:
            if random.randint(1, self.player.speed + self.alien.speed) <= self.player.speed:
                self.player_attack()
                if self.alien.hp > 0:
                    self.alien_attack()
            else:
                self.alien_attack()
                if self.player.hp > 0:
                    self.player_attack()
            print_message(f"You: {self.player.hp} HP")
            print_message(f"{self.alien.name}: {self.alien.hp} HP")
        if self.alien.hp <= 0:
            self.handle_victory()
        else:
            self.handle_defeat()

    def handle_victory(self):
        print_message(f"You killed {self.alien.name}!")
        self.player.hp += 20
        self.player.attack_points += 10
        self.player.speed += 5
        self.player.food += 2
        self.player.enemies_killed += 1
        if random.randint(1, 30) == 21 and not found_glove:
            print_message("You find a mysterious glove!")
            self.player.inventory.append(ARTIFACTS["Shimschnar's Left Hand Glove"])
            print_message(f"You now have {ARTIFACTS['Shimschnar\'s Left Hand Glove']}.")
            found_glove = True

    def handle_defeat(self):
        print_message("You have been defeated.")
        game_over()

    def encounter(self):
        print_message(f"You encounter an alien named {self.alien.name}.")
        print_message(f"{self.alien.name} has a {self.alien.weapon}.")
        print_message("What would you like to do? (attack/run)")
        action = get_input().lower()
        while action not in ["attack", "run"]:
            print_message("Invalid input. Enter 'attack' or 'run'.")
            action = get_input().lower()
        if action == "attack":
            self.fight()
        else:
            self.run()

    def run(self):
        if random.randint(1, self.player.speed + self.alien.speed) <= self.player.speed:
            print_message("You escape successfully.")
        else:
            print_message("You were too slow and the alien attacks you!")
            self.alien_attack()
        self.player.food -= 1

    def player_attack(self):
        self.alien.hp -= self.player.current_weapon.damage
        print_message(self.player.current_weapon.attack_message)

    def alien_attack(self):
        self.player.hp -= self.alien.weapon.damage
        print_message(self.alien.weapon.attack_message)

def create_alien():
    weapon = random.choice(list(ALIEN_WEAPONS.values()))
    name = random.choice(ALIEN_NAMES)
    hp = 20 + (DIFFICULTY * 10)
    speed = 0 + (DIFFICULTY * 10)
    return Alien(name, hp, weapon, speed)

def game_over():
    print_message("Game Over")
    print_message(f"Score: {DIFFICULTY}")
    print_message(f"You made it to day {DAY}.")
    exit()

def play(player):
    global END_GAME, FOUND_GLOVE, REPEAT_SECRET, DAY, DIFFICULTY, CURRENT_ROOM_COUNT
    print_message("You are in the street. You can enter any house numbered 1-10. Enter 'q' to quit.")
    while not END_GAME:
        print_message(player)
        print_message(f"Score: {DIFFICULTY}")
        print_message("Which house would you like to enter? (1-10)")
        house_num = get_input()
        if house_num.lower() == "q":
            END_GAME = True
            break
        try:
            house_num = int(house_num)
            if 1 <= house_num <= 10:
                player.move(house_num)
                CURRENT_ROOM_COUNT += 1
                if CURRENT_ROOM_COUNT == 5:
                    DAY += 1
                    DIFFICULTY += 1
                    CURRENT_ROOM_COUNT = 0
                    print_message(f"It is now day {DAY}. You rest and gain 20 HP.")
                    player.hp += 20
            else:
                print_message("Invalid input. Enter a number between 1 and 10.")
        except ValueError:
            print_message("Invalid input. Enter a number between 1 and 10.")
    game_over()

if __name__ == "__main__":
    player = Player(100, 5, 10, 10, MAP["street"])
    play(player)