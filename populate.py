import os
import time
import sys
import shutil
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alien_game.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

from player_items import weapons, artifacts
from gameApp.models import Weapon, Artifact, UserProfile, Game

WIPE_DATABASE = True
POPULATE_DATABASE = True
CREATE_ADMIN = True
CREATE_USER = True
GENERATE_USERS = True
USER_GENERATION_COUNT = 10
AUTO_RUN_SERVER = False

def django_auto_runserver():
    for x in range(3, 0, -1):
        sys.stdout.write(f'\rAuto-running server in {x} seconds... Ctrl + C to stop.')
        sys.stdout.flush()
        time.sleep(1)
    print("Starting server...")
    call_command('runserver')

def create_superuser(username='test_admin', email='test_admin@admin.com', password='123'):
    print(f'Creating superuser {username}...')
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        admin = User.objects.create_superuser(username=username, email=email, password=password)
        Game.objects.update_or_create(
            user_game=admin,
            defaults={'game_data': '<GameData></GameData>'}
        )
        print(f"Created superuser {username} with game data.")
    else:
        print(f"{username} already exists!")

def create_user(username='test_user', email='test_user@user.com', password='123'):
    print(f'Creating user {username}...')
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, email=email, password=password)
        Game.objects.update_or_create(
            user_game=user,
            defaults={'game_data': '<GameData></GameData>'}
        )
        print(f"Created user {username} with game data.")
    else:
        print(f"{username} already exists!")

def create_easteregg(username='Konami', email='homepage@user.com', password='upupdowndownleftrightleftright'):
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, email=email, password=password)
        game_data = """<GameData>
            <Player>
                <HP>999</HP>
                <AttackPoints>999</AttackPoints>
                <Speed>999</Speed>
                <Food>999</Food>
                <CurrentWeapon>
                    <Name>Katana</Name>
                </CurrentWeapon>
            </Player>
        </GameData>"""
        Game.objects.update_or_create(
            user_game=user,
            defaults={'game_data': game_data}
        )
        
        profile = UserProfile.objects.get(user=user)
        profile.most_enemies_killed = 999
        profile.most_days_survived = 999
        profile.games_played = 999
        profile.artifacts_earned.set(Artifact.objects.all())
        profile.weapons_earned.set(Weapon.objects.all())
        profile.save()
        print(f"Created easteregg user {username} with all items.")
    else:
        print(f"{username} already exists!")

def generate_user_accounts(amount):
    for x in range(amount):
        create_user(f'test_user_{x + 1}', f'test_user_{x + 1}@user.com', '123')

def clean_database_files():
    print('Cleaning up database and media files...')
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
    
    media_dirs = ['media/static/artifact_icons', 'media/static/weapon_icons', 'media/static/user_icons']
    for dir_path in media_dirs:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

def django_auto_migrate():
    clean_database_files()
    call_command('makemigrations')
    call_command('migrate')
    print('Database migrations completed.')

def populate_weapons_and_artifacts():
    print('Populating weapons and artifacts...')
    
    def create_items(model, items, id_field):
        for name, data in items.items():
            item_data = data.copy()
            icon_path = item_data.pop('icon', None)
            
            if icon_path and isinstance(icon_path, str) and os.path.exists(icon_path):
                with open(icon_path, 'rb') as f:
                    item_data['icon'] = File(f, name=os.path.basename(icon_path))
            
            model.objects.update_or_create(
                **{id_field: item_data[id_field]},
                defaults=item_data
            )
    
    create_items(Weapon, weapons, 'weapon_id')
    create_items(Artifact, artifacts, 'artifact_id')
    print('Weapons and artifacts populated successfully.')

if __name__ == '__main__':
    try:
        if WIPE_DATABASE:
            django_auto_migrate()
        if POPULATE_DATABASE:
            populate_weapons_and_artifacts()
        if CREATE_ADMIN:
            create_superuser()
        if CREATE_USER:
            create_user()
            create_easteregg()
            if GENERATE_USERS:
                generate_user_accounts(USER_GENERATION_COUNT)
        if AUTO_RUN_SERVER:
            django_auto_runserver()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)