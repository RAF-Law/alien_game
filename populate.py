import os
import sqlite3

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alien_game.settings')

import django
django.setup()

from django.core.files import File
from gameApp.models import Weapon, Artifact, User, Game

def populate():

    # Weapon Icon Paths - Stored in the same level as alien_game (NOT alien_game/alien_game/)

    weapon_icon_paths = {
        'Weapon1': 'weapon_icons/weapon1.png',
        'Weapon2': 'weapon_icons/weapon2.png',
        'Weapon3': 'weapon_icons/weapon3.png',
    }

    # Define some base weapons (Will be replaced in the future)

    weapons = {
        'Weapon1': {'weapon_id': 1, 'name': 'Weapon1', 'attack_points': 1, 'description': 'Weapon1',
                    'icon': File(open(weapon_icon_paths['Weapon1'], 'rb'))},
        'Weapon2': {'weapon_id': 2, 'name': 'Weapon2', 'attack_points': 2, 'description': 'Weapon2',
                    'icon': File(open(weapon_icon_paths['Weapon2'], 'rb'))},
        'Weapon3': {'weapon_id': 3, 'name': 'Weapon3', 'attack_points': 3, 'description': 'Weapon3',
                    'icon': File(open(weapon_icon_paths['Weapon3'], 'rb'))},
    }

    # Artifact Icon Paths - Stored in the same level as alien_game (NOT alien_game/alien_game/)
    
    artifact_icon_paths = {
        'Artifact1': 'artifact_icons/artifact1.png',
        'Artifact2': 'artifact_icons/artifact2.png',
        'Artifact3': 'artifact_icons/artifact3.png',
    }

    # Define some base artifacts (Will be replaced in the future)

    artifacts = {
        'Artifact1': {'artifact_id': 1, 'name': 'Artifact1', 'description': 'Artifact1',
                      'icon': File(open(artifact_icon_paths['Artifact1'], 'rb'))},
        'Artifact2': {'artifact_id': 2, 'name': 'Artifact2', 'description': 'Artifact2',
                      'icon': File(open(artifact_icon_paths['Artifact2'], 'rb'))},
        'Artifact3': {'artifact_id': 3, 'name': 'Artifact3', 'description': 'Artifact3',
                      'icon': File(open(artifact_icon_paths['Artifact3'], 'rb'))},
    }

    # Define a base game
    
    games = {
        'TestGame1': {'game_id': 1, 'player_hp': 100, 'player_ap': 10, 'player_speed': 1, 'player_food': 10, 'game_enemies_killed': 0, 'game_day': 1, 'game_difficulty': 1, 'game_map': 1}
    }

    users = {
        'TestUser1': {'user_id': 1, 'most_enemies_killed': 0, 'most_days_survived': 0, 'games_played': 0}
    }

    # Define functions for populating database with weapons, artifacts, games and users

    def populate_weapons():
        for weapon_name, weapon_data in weapons.items():
            weapon = Weapon.objects.get_or_create(
                weapon_id=weapon_data['weapon_id'],
                name=weapon_data['name'],
                attack_points=weapon_data['attack_points'],
                description=weapon_data['description'],
                icon=weapon_data['icon']
            )[0]

    def populate_artifacts():
        for artifact_name, artifact_data in artifacts.items():
            artifact = Artifact.objects.get_or_create(
                artifact_id=artifact_data['artifact_id'],
                name=artifact_data['name'],
                description=artifact_data['description'],
                icon=artifact_data['icon'],
            )[0]

    def populate_games():
        for game_name, game_data in games.items():
            game = Game.objects.get_or_create(
                game_id=game_data['game_id'],
                player_hp=game_data['player_hp'],
                player_ap=game_data['player_ap'],
                player_speed=game_data['player_speed'],
                player_food=game_data['player_food'],
                game_enemies_killed=game_data['game_enemies_killed'],
                game_day=game_data['game_day'],
                game_difficulty=game_data['game_difficulty'],
                game_map=game_data['game_map']
            )[0]

    def populate_users():
        for user_name, user_data in users.items():
            user = User.objects.get_or_create(
                user_id=user_data['user_id'],
                most_enemies_killed=user_data['most_enemies_killed'],
                most_days_survived=user_data['most_days_survived'],
                games_played=user_data['games_played']
            )[0]

    # Run functions and handle duplicate entries when database is already populated (doesn't work)
    
    try:

        populate_users()
        populate_games()
        populate_weapons()
        populate_artifacts()

    except sqlite3.IntegrityError:
        print('Skipping duplicate entry...')
        pass

    # If you reached here, the code ran correctly
    
    print('Database populated!')

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
