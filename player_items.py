from django.core.files.base import File

static_weapon_path = 'static/weapon_icons/'
static_artifact_path = 'static/artifact_icons/'

weapon_icon_paths = {
        "Ak-47": "Ak-47.png",
        "Baseball Bat": "Baseball Bat.png",
        "Laser Gun": "Laser Gun.png",
        "Plasma Rifle": "Plasma Rifle.png",
        "Energy Sword": "Energy Sword.png",
        "Flamethrower": "Flamethrower.png",
        "Railgun": "Railgun.png",
        "Katana": "Katana.png",
        "Chicken": "Chicken.png",
        "Revolver": "Revolver.png",
        "Shotgun": "Shotgun.png",
    }

artifact_icon_paths = {
    "Cosmic Crystal": "Cosmic Crystal.png",
    "Galactic Map": "Galactic Map.png",
    "Alien Artifact": "Alien Artifact.png",
    "Extraterrestrial Coin": "Extraterrestrial Coin.png",
    "Space Helmet": "Space Helmet.png",
    "Alien Skull": "Alien Skull.png",
    "Stardust": "Stardust.png",
    "Meteorite Fragment": "Meteorite Fragment.png",
    "Alien Fossil": "Alien Fossil.png",
    "Space Gem": "Space Gem.png",
    "Alien Egg": "Alien Egg.png",
    "Cosmic Dust": "Cosmic Dust.png",
    "Alien Amulet": "Alien Amulet.png",
    "Galactic Artifact": "Galactic Artifact.png",
    "Space Relic": "Space Relic.png",
    "Alien Crystal": "Alien Crystal.png",
    "Extraterrestrial Relic": "Extraterrestrial Relic.png",
    "Shimschnar's Left Hand Glove": "Shimschnar's Left Hand Glove.png",
    "The Dictionary of the Ancients": "The Dictionary of the Ancients.png",
    "The Orb of Time": "The Orb of Time.png",
    "The Eye of Schmelborg": "The Eye of Schmelborg.png",
}


weapons = {
    "Ak-47": {
        'weapon_id': 1,
        'name': "Ak-47",
        'damage': 40,
        'description': "A powerful assault Rifle",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Ak-47"], 'rb')),
        'rarity': 2,
        'attack_message': "You shoot the alien with your Ak-47",
    },
    "Baseball Bat": {
        'weapon_id': 2,
        'name': "Baseball Bat",
        'damage': 15,
        'description': "A wooden baseball bat with barbed wire wrapped around it",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Baseball Bat"], 'rb')),
        'rarity': 1,
        'attack_message': "You hit the alien with your gruesome baseball bat",
    },
    "Laser Gun": {
        'weapon_id': 3,
        'name': "Laser Gun",
        'damage': 50,
        'description': "A futuristic laser weapon not of this world",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Laser Gun"], 'rb')),
        'rarity': 2,
        'attack_message': "You zap the alien with your Laser Gun",
    },
    "Plasma Rifle": {
        'weapon_id': 4,
        'name': "Plasma Rifle",
        'damage': 60,
        'description': "A high-tech energy charged rifle",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Plasma Rifle"], 'rb')),
        'rarity': 3,
        'attack_message': "You blast the alien with your Plasma Rifle",
    },
    "Energy Sword": {
        'weapon_id': 5,
        'name': "Energy Sword",
        'damage': 75,
        'description': "A sword made of pure energy that emits a loud hum",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Energy Sword"], 'rb')),
        'rarity': 3,
        'attack_message': "You slash the alien with your Energy Sword",
    },
    "Flamethrower": {
        'weapon_id': 6,
        'name': "Flamethrower",
        'damage': 55,
        'description': "A weapon that shoots flames, incinerating enemies",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Flamethrower"], 'rb')),
        'rarity': 2,
        'attack_message': "You burn the alien with your Flamethrower",
    },
    "Railgun": {
        'weapon_id': 7,
        'name': "Railgun",
        'damage': 90,
        'description': "A powerful electromagnetic weapon that can fire from up to 65 kilometres away",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Railgun"], 'rb')),
        'rarity': 3,
        'attack_message': "You blow a hole through the alien with your Railgun",
    },
    "Katana": {
        'weapon_id': 8,
        'name': "影の龍",
        'damage': 100,
        'description': "A katana that was passed down through many generations of honorable samurai",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Katana"], 'rb')),
        'rarity': 4,
        'attack_message': "You slice through the alien with unheavenly precision",
    },
    "Chicken": {
        'weapon_id': 9,
        'name': "Chicken",
        'damage': 10,
        'description': "A chicken that attacks aliens for some reason",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Chicken"], 'rb')),
        'rarity': 1,
        'attack_message': "You throw the chicken at the alien",
    },
    "Revolver": {
        'weapon_id': 10,
        'name': "Revolver",
        'damage': 25,
        'description': "A six-shooter revolver",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Revolver"], 'rb')),
        'rarity': 1,
        'attack_message': "You shoot the alien with your revolver",
    },
    "Shotgun": {
        'weapon_id': 11,
        'name': "Shotgun",
        'damage': 45,
        'description': "A shotgun that fires a spread of pellets",
        'icon': File(open(static_weapon_path + weapon_icon_paths["Shotgun"], 'rb')),
        'rarity': 2,
        'attack_message': "You blast the alien with your shotgun",
    },
}

artifacts = {
    "Cosmic Crystal": {
        'artifact_id': 1,
        'name': "Cosmic Crystal",
        'description': "A crystal that glows with an otherworldly light",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Cosmic Crystal"], 'rb')),
        'rarity': 3,
    },
    "Galactic Map": {
        'artifact_id': 2,
        'name': "Galactic Map",
        'description': "A map showing the locations of alien worlds",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Galactic Map"], 'rb')),
        'rarity': 2,
    },
    "Alien Artifact": {
        'artifact_id': 3,
        'name': "Alien Artifact",
        'description': "An artifact of unknown origin and purpose",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Alien Artifact"], 'rb')),
        'rarity': 1,
    },
    "Extraterrestrial Coin": {
        'artifact_id': 4,
        'name': "Extraterrestrial Coin",
        'description': "A coin from an alien currency",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Extraterrestrial Coin"], 'rb')),
        'rarity': 1,
    },
    "Space Helmet": {
        'artifact_id': 5,
        'name': "Space Helmet",
        'description': "A helmet worn by an alien astronaut",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Space Helmet"], 'rb')),
        'rarity': 2,
    },
    "Alien Skull": {
        'artifact_id': 6,
        'name': "Alien Skull",
        'description': "The skull of a long-dead alien",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Alien Skull"], 'rb')),
        'rarity': 3,
    },
    "Stardust": {
        'artifact_id': 7,
        'name': "Stardust",
        'description': "A handful of glowing stardust",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Stardust"], 'rb')),
        'rarity': 1,
    },
    "Meteorite Fragment": {
        'artifact_id': 8,
        'name': "Meteorite Fragment",
        'description': "A fragment of a meteorite",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Meteorite Fragment"], 'rb')),
        'rarity': 2,
    },
    "Alien Fossil": {
        'artifact_id': 9,
        'name': "Alien Fossil",
        'description': "A fossilized alien creature",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Alien Fossil"], 'rb')),
        'rarity': 3,
    },
    "Space Gem": {
        'artifact_id': 10,
        'name': "Space Gem",
        'description': "A gem from outer space",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Space Gem"], 'rb')),
        'rarity': 2,
    },
    "Alien Egg": {
        'artifact_id': 11,
        'name': "Alien Egg",
        'description': "An egg containing an alien lifeform",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Alien Egg"], 'rb')),
        'rarity': 1,
    },
    "Cosmic Dust": {
        'artifact_id': 12,
        'name': "Cosmic Dust",
        'description': "A small amount of cosmic dust",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Cosmic Dust"], 'rb')),
        'rarity': 1,
    },
    "Alien Amulet": {
        'artifact_id': 13,
        'name': "Alien Amulet",
        'description': "An amulet with alien symbols",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Alien Amulet"], 'rb')),
        'rarity': 2,
    },
    "Galactic Artifact": {
        'artifact_id': 14,
        'name': "Galactic Artifact",
        'description': "An artifact from another galaxy",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Galactic Artifact"], 'rb')),
        'rarity': 3,
    },
    "Space Relic": {
        'artifact_id': 15,
        'name': "Space Relic",
        'description': "A relic from outer space",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Space Relic"], 'rb')),
        'rarity': 2,
    },
    "Alien Crystal": {
        'artifact_id': 16,
        'name': "Alien Crystal",
        'description': "A crystal with alien properties",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Alien Crystal"], 'rb')),
        'rarity': 3,
    },
    "Extraterrestrial Relic": {
        'artifact_id': 17,
        'name': "Extraterrestrial Relic",
        'description': "A relic from an extraterrestrial civilization",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Extraterrestrial Relic"], 'rb')),
        'rarity': 2,
    },
    "Shimschnar's Left Hand Glove": {
        'artifact_id': 18,
        'name': "Shimschnar's Left Hand Glove",
        'description': "The left hand glove of the legendary alien warrior Shimschnar, it's true ability is unknown",
        'icon': File(open(static_artifact_path + artifact_icon_paths["Shimschnar's Left Hand Glove"], 'rb')),
        'rarity': 4,
    },
    "The Dictionary of the Ancients": {
        'artifact_id': 19,
        'name': "The Dictionary of the Ancients",
        'description': "A book containing the language of an ancient alien civilization",
        'icon': File(open(static_artifact_path + artifact_icon_paths["The Dictionary of the Ancients"], 'rb')),
        'rarity': 4,
    },
    "The Orb of Time": {
        'artifact_id': 20,
        'name': "The Orb of Time",
        'description': "An orb that can manipulate time itself, but you have no idea how it works",
        'icon': File(open(static_artifact_path + artifact_icon_paths["The Orb of Time"], 'rb')),
        'rarity': 4,
    },
    "The Eye of Schmelborg": {
        'artifact_id': 21,
        'name': "The Eye of Schmelborg",
        'description': "While conquering planets, Schmelborg lost his eye. Now you found it. Well done I guess.",
        'icon': File(open(static_artifact_path + artifact_icon_paths["The Eye of Schmelborg"], 'rb')),
        'rarity': 6,
    }
}