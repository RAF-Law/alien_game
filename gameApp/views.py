# View imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
import json

# Authenication imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Model imports
from gameApp.models import UserProfile as User
from gameApp.models import Game
from gameApp.models import Weapon
from gameApp.models import Artifact

# Forms import 
from gameApp.forms import UserForm
from gameApp.forms import UserProfileForm



# HomePage view 
# Visible to ALL users
# URL: gameApp/
# Template: gameApp/home.html
def home(request):
    context_dict={}
    return render(request, 'gameApp/home.html', context=context_dict)


# Instructions view
# Visiblity: ALL users
# URL: gameApp/instructions/
# Template: gameApp/instructions.html
def instructions(request):
    context_dict={}
    return render(request, 'gameApp/instructions.html', context=context_dict)


# Register view
# Visiblity: UNAUTHENTICATED users
# URL: gameApp/register/
# Template: gameApp/register.html
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'icon' in request.FILES:
                profile.icon = request.FILES['icon']

            profile.save()

            registered = True
        else:
            errors = {
                'user_form_errors': user_form.errors.as_json(),
                'profile_form_errors': profile_form.errors.as_json()
            }
            return JsonResponse({'status': 'error', 'errors': errors})

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'gameApp/register.html', context = {'user_form': user_form,
                                                               'profile_form': profile_form,
                                                                'registered': registered,})


# Login view
# Visiblity: UNAUTHENTICATED users
# URL: gameApp/login/
# Template: gameApp/login.html
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                user_profile = User.objects.get(user=user)
                response = redirect(reverse("gameApp:home"))
                if "easteregg" in request.COOKIES:
                    eastereggArtifact = Artifact.objects.get(artifact_id=21)
                    user_profile.artifacts_earned.add(eastereggArtifact)  # Django ignores if already exists
                    if request.user.username != "Konami":
                        response.delete_cookie("easteregg")
                return response
            else:
                return HttpResponse("Your Account has been disabled :[]") #I dont think this part will be used
        else:
            return JsonResponse({"status": "error", "message": "Invalid login details."})
    else:
        return render(request, 'gameApp/login.html')


# Logout
# Visiblity: AUTHENTICATED users
# URL: Null
# Template: Null
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('gameApp:home'))


# Account view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/
# Template: gameApp/user_account.html
@login_required
def user_account(request):
    user_profile = User.objects.get(user=request.user)

    response = render(request, 'gameApp/user_account.html', {
        'profile_form': UserProfileForm(instance=user_profile),
        'user_profile': user_profile,
    })

    # Handle profile form submission
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse('gameApp:user_account'))  # Reload page after updating PFP

    return response



# User History view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/my_history/
# Template: gameApp/user_history.html
@login_required
def user_history(request):

    user_information = User.objects.get(user=request.user)

    context_dict={}
    context_dict['user_history'] = user_information.history_games

    return render(request, 'gameApp/user_history.html', context=context_dict)


# User Handbook view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/my_handbook/
# Template: gameApp/user_handbook.html
@login_required
def user_handbook(request):
    user_profile = User.objects.get(user=request.user)
    response = render(request, 'gameApp/user_handbook.html')  

    # Get user-specific and all artifacts
    user_artifacts_list = user_profile.artifacts_earned.all()
    artifacts_list = Artifact.objects.all()

    # Get user-specific and all weapons
    user_weapons_list = user_profile.weapons_earned.all()
    weapons_list = Weapon.objects.all()

    context_dict = {
        'user_artifacts': user_artifacts_list,
        'artifacts': artifacts_list,
        'user_weapons': user_weapons_list,
        'weapons': weapons_list
    }

    response = render(request, 'gameApp/user_handbook.html', context=context_dict)
    return response


# Leaderboard view
# Visiblity: ALL users
# URL: gameApp/leaderboard/
# Template: gameApp/leaderboard.html
def leaderboard(request):

    # Get top 8 players with most kills
    player_enemies_list = User.objects.order_by('-most_enemies_killed')[:8] 
    # Get top 8 players with most days survived
    player_days_list = User.objects.order_by('-most_days_survived')[:8] 

    # Store player lists into context dictionary, to be used in html
    context_dict={}
    context_dict['player_enemies'] = player_enemies_list
    context_dict['player_days'] = player_days_list

    return render(request, 'gameApp/leaderboard.html', context=context_dict)


# Play view
# Visiblity: AUTHENTICATED users
# URL: gameApp/play/
# Template: gameApp/play.html
@login_required
def play(request):
    context_dict={}
    return render(request, 'gameApp/play.html', context=context_dict)


# Game Scene view
# Visiblity: AUTHENTICATED users
# URL: gameApp/play/gameScene/
# Template: gameApp/gameScene.html
@login_required
def gameScene(request):
    user_profile = User.objects.get(user=request.user)
    context_dict = {'user_profile': user_profile,}
    return render(request, 'gameApp/gameScene.html', context= context_dict)

@login_required
def gameCreation(request):
    user_profile = User.objects.get(user=request.user)
    context_dict = {'user_profile': user_profile,}
    game = Game.objects.get(user_game=request.user)
    game.game_data = '<GameData><Player><HP>100</HP><AttackPoints>5</AttackPoints><Speed>10</Speed><Food>10</Food><EnemiesKilled>0</EnemiesKilled><Location>street</Location><CurrentWeapon><Name>Fists</Name></CurrentWeapon><Inventory/></Player><Map><EmptyHouses/><House name="house 1"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 2"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 3"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 4"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 5"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 6"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 7"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 8"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 9"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House><House name="house 10"><TimesEntered>0</TimesEntered><Rooms/><EmptyRooms/></House></Map><SecretsFound><Secret name="The Orb of Time">false</Secret><Secret name="The Glove of Power">false</Secret><Secret name="Katana">false</Secret><Secret name="Dictionary">false</Secret></SecretsFound><GameProgress><Day>1</Day><Difficulty>1</Difficulty><CurrentRoomCount>0</CurrentRoomCount><MaxHP>100</MaxHP></GameProgress></GameData>'
    game.save()
    return redirect("gameApp:gameScene")

def easteregg(request):
    try:
        current_user = User.objects.get(user=request.user)
        if current_user:
            logout(request)
    finally:
        easteregguser = authenticate(username="Konami", password="upupdowndownleftrightleftright")
        login(request, easteregguser)
        response = redirect(reverse("gameApp:home"))
        response.set_cookie("easteregg", "0")
        return response

weapons = { #reserved for lookup
    "Ak-47": {'weapon_id': 1,},
    "Baseball Bat": {'weapon_id': 2,},
    "Laser Gun": {'weapon_id': 3,},
    "Plasma Rifle": {'weapon_id': 4,},
    "Energy Sword": {'weapon_id': 5,},
    "Flamethrower": {'weapon_id': 6,},
    "Railgun": {'weapon_id': 7,},
    "Katana": {'weapon_id': 8,},
    "Chicken": {'weapon_id': 9,},
    "Revolver": {'weapon_id': 10,},
    "Shotgun": {'weapon_id': 11,}
    }
artifacts = {
    "Cosmic Crystal": {'artifact_id': 1,},
    "Galactic Map": {'artifact_id': 2,},
    "Alien Artifact": {'artifact_id': 3,},
    "Extraterrestrial Coin": {'artifact_id': 4,},
    "Space Helmet": {'artifact_id': 5,},
    "Alien Skull": {'artifact_id': 6,},
    "Stardust": {'artifact_id': 7,},
    "Meteorite Fragment": {'artifact_id': 8,},
    "Alien Fossil": {'artifact_id': 9,},
    "Space Gem": {'artifact_id': 10,},
    "Alien Egg": {'artifact_id': 11,},
    "Cosmic Dust": {'artifact_id': 12,},
    "Alien Amulet": {'artifact_id': 13,},
    "Galactic Artifact": {'artifact_id': 14,},
    "Space Relic": {'artifact_id': 15,},
    "Alien Crystal": {'artifact_id': 16,},
    "Extraterrestrial Relic": {'artifact_id': 17,},
    "Shimschnar's Left Hand Glove": {'artifact_id': 18,},
    "The Dictionary of the Ancients": {'artifact_id': 19,},
    "The Orb of Time": {'artifact_id': 20,},
    "The Eye of Schmelborg": {'artifact_id': 21}
    }
def get_weapon_image(request, weapon_name): #I MADE IT WORK I'M CRYING
    id = weapons[weapon_name]["weapon_id"]
    weapon = Weapon.objects.get(weapon_id=id)
    return JsonResponse({"image_url": weapon.icon.url})

@login_required
def save_history(request):
    if request.method == "POST":
        try:
            #get data from js
            data = json.loads(request.body)
            enemies_killed = data.get("enemies_killed")
            days_survived = data.get("days_survived")
            max_hp = data.get("max_hp")
            inv = data.get("inventory")

            #database update
            user_profile = User.objects.get(user=request.user)
            user_profile.update_most_enemies_killed(enemies_killed)
            user_profile.update_most_days_survived(days_survived)
            user_profile.increment_games_played()
            user_profile.history_games.append([enemies_killed,days_survived,max_hp,str(timezone.now())])
            for i in inv:
                try:
                    id = weapons[i]["weapon_id"]
                    weapon = Weapon.objects.get(weapon_id=id)
                    user_profile.weapons_earned.add(weapon)
                except:
                    id = artifacts[i]["artifact_id"]
                    artifact = Artifact.objects.get(artifact_id=id)
                    user_profile.artifacts_earned.add(artifact)
            
            user_profile.save()

            #return
            return JsonResponse({"status": "success", "message": "Game results saved!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=405)

@login_required
def save_game_state(request):
     if request.method == "POST":
         try:
             data = json.loads(request.body)
             xml_data = data.get("game_data")
             game = Game.objects.get(user_game=request.user)
             game.game_data = xml_data
             game.save()
             
             return JsonResponse({"status": "success", "message": "Game saved successfully!"})
         except Exception as e:
             return JsonResponse({"status": "error", "message": str(e)}, status=400)
     return JsonResponse({"status": "error", "message": "Invalid request"}, status=405)

@login_required
def load_game_state(request):
     try:
         game = Game.objects.get(user_game=request.user)
         return HttpResponse(game.game_data, content_type="application/xml")
     except Game.DoesNotExist:
         return JsonResponse({
             "status": "error",
             "message": "No saved game found"
         }, status=404)
     except Exception as e:
         return JsonResponse({
             "status": "error",
             "message": str(e)
         }, status=400)