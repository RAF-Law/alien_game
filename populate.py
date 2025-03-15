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
from gameApp.models import Weapon, Artifact, UserProfile as User, Game

WIPE_DATABASE = True
POPULATE_DATABASE = True
CREATE_ADMIN = True
CREATE_USER = True
GENERATE_USERS = True
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

    print(f'Creating superuser {username}...')
    user = get_user_model()
    if not user.objects.filter(username=username).exists():
        user.objects.create_user(username=username, email=email, password=password)
        print(f"Created user {username}.")
    else:
        print(f"{username} already exists!")

def generate_user_accounts(amount):
    for x in range(amount):
        create_user(f'test_user_{x}', f'test_user_{x}@user.com', f'123')


def check_database_exists():

    print('Checking if database exists...')
    db_path = 'db.sqlite3'
    if os.path.exists(db_path):
        print('db.sqlite3 exists, deleting...')
        os.remove(db_path)
    else:
        print('Database does not exist.')

    db_weapon_icon_path = 'media/static/artifact_icons/static/artifact_icons'
    db_artifact_icon_path = 'media/static/weapon_icons/static/weapon_icons'
    db_user_icon_path = 'media/static/user_icons/static/user_icons'

    print('Checking if weapon, artifact and user icon duplicates exist...')

    if os.path.exists(db_weapon_icon_path):
        print('Weapon icon duplicates exist, deleting...')
        shutil.rmtree(db_weapon_icon_path)

    if os.path.exists(db_artifact_icon_path):
        print('Artifact icon duplicates exist, deleting...')
        shutil.rmtree(db_artifact_icon_path)

    if os.path.exists(db_user_icon_path):
        print('User icon duplicates exist, deleting...')
        shutil.rmtree(db_user_icon_path)

def django_auto_migrate():

    print('Setting up prerequisites...')
    check_database_exists()
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
        if GENERATE_USERS:
            generate_user_accounts(10)
    if AUTO_RUN_SERVER:
        django_auto_runserver()
