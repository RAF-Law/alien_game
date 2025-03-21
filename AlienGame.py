import random
import time
from flask import Flask, request, jsonify

MOCK_WEAPONS = (
    {"name": "Sword", "description": "A sharp blade.", "damage": 10, "attack_message": "You slash the enemy.", "rarity": 2},
    {"name": "Bow", "description": "A ranged weapon.", "damage": 8, "attack_message": "You shoot an arrow.", "rarity": 1},
    {"name": "Axe", "description": "A heavy weapon.", "damage": 15, "attack_message": "You chop the enemy.", "rarity": 3},
)

MOCK_ARTIFACTS = (
    {"name": "Amulet of Power", "description": "Increases your strength.", "rarity": 4},
    {"name": "Ring of Speed", "description": "Makes you faster.", "rarity": 3},
    {"name": "Cloak of Invisibility", "description": "Makes you invisible.", "rarity": 5},
    {"name": "The Orb of Time", "description": "Makes you sigma.", "rarity": 5},
)

def fetch_weapons():
    weapons = {}
    for weapon_data in MOCK_WEAPONS:
        weapon = Weapon(
            name=weapon_data["name"],
            description=weapon_data["description"],
            damage=weapon_data["damage"],
            attack_message=weapon_data["attack_message"],
            rarity=weapon_data["rarity"]
        )
        weapons[weapon.name] = weapon
    return weapons

def fetch_artifacts():
    artifacts = {}
    for artifact_data in MOCK_ARTIFACTS:
        artifact = Artifact(
            name=artifact_data["name"],
            description=artifact_data["description"],
            rarity=artifact_data["rarity"]
        )
        artifacts[artifact.name] = artifact
    return artifacts

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

RARITIES = {1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic", 5: "Legendary"}

ALIEN_WEAPONS = {
    "Goppin": Weapon("Goppin", "A weapon that fires plasma.", 5, "The alien shoots you with plasma.", 1),
    "Sponk": Weapon("Sponk", "A weapon that fires energy bursts.", 15, "The alien blasts you with energy.", 2),
    "Zorblax": Weapon("Zorblax", "A weapon that shoots energy beams.", 25, "The alien fires a beam at you.", 3),
}

ALIEN_NAMES = ("Zog", "Gorp", "Prip", "Geggin", "Nairn", "Hojjim", "Kada")

end_game = False
day = 1
difficulty = 1
current_room_count = 0

WEAPONS = fetch_weapons()
ARTIFACTS = fetch_artifacts()

map = {
    "street": "street",
    "empty_houses": set(),
    **{f"house {i}": {"empty_rooms": set(), "times_entered": 0} for i in range(1, 11)},
}

app = Flask(__name__)

@app.route('/get_message', methods=['GET'])
def print_message(message):
    #return jsonify({"messages" : message})
    global current_message
    current_message += message + "\n"

def send_message(choices):
    global current_message
    pack = jsonify({"messages" : current_message, "options" : choices})
    current_message = ""
    return pack


@app.route('/send_input', methods=['POST'])
def get_input():
    user_input = request.json.get("user_input", "")
    return user_input.strip()
    #return input().strip()

class Room:
    def __init__(self, room_type, alien=None):
        self.loot = set()
        self.room_type = room_type
        self.alien = alien

    def generate_loot(self, items, rarity_cap):
        loot_num = random.randint(0, 2)
        for _ in range(loot_num):
            item = random.choice(list(items.values()))
            if item.rarity <= rarity_cap and item not in self.loot:
                self.loot.add(item)

    def search_room(self, player):

        match self.room_type:
            case 0:
                print_message("This room is empty.")
            case 1:
                self.generate_loot(WEAPONS, random.randint(1, 3))
            case 2:
                self.generate_loot(ARTIFACTS, random.randint(1, 3))
            case 3:
                if self.alien is None:
                    self.alien = create_alien()
                Battle(player, self.alien).encounter()
                return
            case _:
                print_message("Invalid room type.")
                return

def handle_loot(self, player, loot_type):
    print_message(f"You find yourself in a room filled with {loot_type}s.")

    #time.sleep(1)
    print_message("You search the room and find:")

    #time.sleep(1)
    for index, item in enumerate(self.loot):
        print_message(f"{index + 1}: {item}")
        #time.sleep(1)

    print_message("Would you like to take any of these items?")
    send_message("yes/no")

    def get_choice():

        user_input = get_input().lower().strip()

        if user_input not in ("yes", "no", "q", "y", "n"):
            print_message("Invalid input. Enter 'yes', 'no', or 'q' to quit.")
            send_message("yes/no/q")
            get_choice()

        return user_input

    choice = get_choice()

    match choice:
        case "yes", "y":
            print_message(f"Which {loot_type} would you like to take?")
            sending_msg = ""
            for i in range(len(self.loot)):
                sending_msg += str(i+1) + "/"
            send_message(sending_msg)

            try:
                item_choice = int(get_input()) - 1
                selected_item = self.loot[item_choice]
                if loot_type == "weapon":
                    player.current_weapon = selected_item
                else:
                    player.inventory.add(selected_item)
                print_message(f"You now have {selected_item.name}.")
                player.food -= 1
                print_message("It cost you 1 Food.")
            except (IndexError, ValueError):
                print_message("Invalid selection.")

        case "no", "n":
            print_message("You decide not to take any items.")
            return
        case "q":
            global end_game
            end_game = True
            return
        case _:
            self.handle_loot(player, loot_type)
            return

class Player:
    def __init__(self, hp, attack_points, speed, food, location):
        self.hp = hp
        self.attack_points = attack_points
        self.current_weapon = Weapon("Fists", "Your fists", attack_points, "You punch the alien.", 1)
        self.inventory = set()
        self.speed = speed
        self.food = food
        self.location = location
        self.enemies_killed = 0
        self.secrets_found = {
            "The Orb of Time": False,
            "The Glove of Power": False,
        }

    def __str__(self):
        return f"HP: {self.hp} | Attack Points: {self.attack_points} | Speed: {self.speed} | Food: {self.food}"

    def move(self, house):
        house_key = f"house {house}"

        if house_key in map["empty_houses"]:
            print_message("This house is empty.")
            return

        map[house_key]["times_entered"] += 1

        if map[house_key]["times_entered"] == 5 and not self.secrets_found['The Orb of Time']:

            print_message("You have spent so much time in this house that you find a hidden artifact!")
            #time.sleep(1)
            player.inventory.add(ARTIFACTS["The Orb of Time"])
            print_message(f"You now have {ARTIFACTS['The Orb of Time']}.")

            self.secrets_found['The Orb of Time'] = True

        else:
            print_message(f"You enter {house_key}.")
            self.explore_house(house_key)

    def explore_house(self, house_key):

        num_rooms = random.randint(2, 6)

        for i in range(1, num_rooms + 1):
            room_key = f"room {i}"
            room_type = random.randint(0, 3)
            map[house_key][room_key] = Room(room_type)

        print_message(f"There are {num_rooms} rooms in this house. Which room would you like to enter?")
        sending_msg = ""
        for i in range(num_rooms):
            sending_msg + str(i+1) + "/"

        room_num = int(get_input())
        room_key = f"room {room_num}"

        self.location = map[house_key][room_key]
        self.location.search_room(self)

        if room_key not in map[house_key]["empty_rooms"]:
            map[house_key]["empty_rooms"].add(room_key)
        if len(map[house_key]["empty_rooms"]) == num_rooms:
            print_message("You have emptied all rooms in this house.")
            map["empty_houses"].add(house_key)

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

            #time.sleep(1)
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

        if random.randint(1, 30) == 21 and not self.player.secrets_found['The Glove of Power']:
            print_message("You find a mysterious glove!")
            self.player.inventory.add(ARTIFACTS["Shimschnar's Left Hand Glove"])
            print_message(f"You now have {ARTIFACTS['Shimschnar\'s Left Hand Glove']}.")
            self.player.secrets_found['The Glove of Power'] = True

    def handle_defeat(self):
        print_message("You have been defeated.")
        game_over()

    def encounter(self):
        print_message(
            f"You encounter an alien named {self.alien.name}.\n"
            f"{self.alien.name} has a {self.alien.weapon}.\n"
            "What would you like to do?"
        )
        send_message("attack/run")

        def get_choice():
            while True:
                user_input = get_input().lower().strip()
                if user_input in ("attack", "run", "a", "r"):
                    return user_input
                else:
                    print_message("Invalid input. Enter 'attack' or 'run'.")

        action = get_choice()

        if action in ("attack", "a"):
            self.fight()
        elif action in ("run", "r"):
            self.run()

    def run(self):
        if random.randint(1, self.player.speed + self.alien.speed) <= self.player.speed:
            print_message("You escape successfully.")
        else:
            print_message(f"You were too slow and {self.alien.name} attacks you!")
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
    hp = 20 + (difficulty * 10)
    speed = 0 + (difficulty * 10)
    return Alien(name, hp, weapon, speed)

def game_over():
    print_message("Game Over")
    print_message(f"Score: {difficulty}")
    print_message(f"You made it to day {day}.")
    exit()

def play(player):
    global end_game, day, difficulty, current_room_count
    print_message("You are in the street. You can enter any house numbered 1-10. Enter 'q' to quit.")
    while not end_game:
        print_message(player)
        print_message(f"Score: {difficulty}")
        print_message("Which house would you like to enter? (1-10)")
        send_message("1/2/3/4/5/6/7/8/9/10/q")
        house_num = get_input()
        if house_num.lower() == "q":
            end_game = True
            break
        try:
            house_num = int(house_num)
            if 1 <= house_num <= 10:
                player.move(house_num)
                current_room_count += 1
                if current_room_count == 5:
                    day += 1
                    difficulty += 1
                    current_room_count = 0
                    print_message(f"It is now day {day}. You rest and gain 20 HP.")
                    player.hp += 20
            else:
                print_message("Invalid input. Enter a number between 1 and 10.")
        except ValueError:
            print_message("Invalid input. Enter a number between 1 and 10.")
    game_over()

if __name__ == "__main__":
    player = Player(100, 5, 10, 10, map["street"])
    play(player)
