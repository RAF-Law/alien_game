import os
import time
import sys
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alien_game.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

from player_items import weapons, artifacts
from gameApp.models import Weapon, Artifact, UserProfile

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
    user = get_user_model()
    if not user.objects.filter(username=username).exists():
        user.objects.create_superuser(username=username, email=email, password=password)
        print(f"Created superuser {username}.")
    else:
        print(f"{username} already exists!")

def create_user(username='test_user', email='test_user@user.com', password='123'):

    print(f'Creating user {username}...')
    user = get_user_model()
    if not user.objects.filter(username=username).exists():
        user.objects.create_user(username=username, email=email, password=password)
        print(f"Created user {username}.")
    else:
        print(f"{username} already exists!")

def create_easteregg(username='Konami', email='homepage@user.com', password='upupdowndownleftrightleftright'):
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = UserProfile.objects.get(user=user)
        profile.most_enemies_killed = -1
        profile.most_days_survived = -1
        profile.games_played = -1
        artifacts = Artifact.objects.all()
        weapons = Weapon.objects.all()
        profile.artifacts_earned.add(*artifacts)
        profile.weapons_earned.add(*weapons)
        profile.save()

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

    print('Setting up prerequisites...')
    clean_database_files()
    call_command('makemigrations')
    call_command('migrate')
    print('Prerequisites set up!')

def populate_database():

    print('Starting database population script...')

    def populate_model(model, data, unique_field):

        for item_name, item_data in data.items():
            model.objects.get_or_create(**{unique_field: item_data[unique_field]}, defaults=item_data)

    try:

        populate_model(Weapon, weapons, 'weapon_id')
        populate_model(Artifact, artifacts, 'artifact_id')

    except Exception as e:
        print(f'Error: {str(e)}, re-wiping database and stopping execution.')
        django_auto_migrate()
        return False

    print('Database populated!')
    return True

if __name__ == '__main__':

    if WIPE_DATABASE:
        django_auto_migrate()
    if POPULATE_DATABASE:
        populate_database()
    if CREATE_ADMIN:
        create_superuser()
    if CREATE_USER:
        create_user()
        create_easteregg()
        if GENERATE_USERS:
            generate_user_accounts(USER_GENERATION_COUNT)
    if AUTO_RUN_SERVER:
        django_auto_runserver()
