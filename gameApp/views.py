# View imports
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

# Authenication imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Model imports
from gameApp.models import User
from gameApp.models import Game
from gameApp.models import Weapon
from gameApp.models import Artifact


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
    context_dict={}
    return render(request, 'gameApp/register.html', context=context_dict)


# Login view
# Visiblity: UNAUTHENTICATED users
# URL: gameApp/login/
# Template: gameApp/login.html
def user_login(request):
    context_dict={}
    return render(request, 'gameApp/user_login.html', context=context_dict)


# Logout
# Visiblity: AUTHENTICATED users
# URL: Null
# Template: Null
def user_logout(request):
    logout(request)
    return redirect(reverse('gameApp:home'))


# Account view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/
# Template: gameApp/user_account.html
def user_account(request):
    # Pass in user specific information 
    context_dict={}
    return render(request, 'gameApp/user_account.html', context=context_dict)


# User History view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/my_history/
# Template: gameApp/user_history.html
def user_history(request):

    # pass in user specific history info
    user_information = User.objects.get(request.user)

    # Store user specific information into context dictionary
    context_dict={}
    context_dict['user_info'] = user_information

    return render(request, 'gameApp/user_history.html', context=context_dict)


# User Handbook view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/my_handbook/
# Template: gameApp/user_handbook.html
def user_handbook(request):

    # Get user specific artifacts earned
    user_artifacts_list = User.objects.get('-artifacts_earned')
    # Get all artifacts 
    artifacts_list = Artifact.objects.all()

    # Get user specific weapons earned
    user_weapons_list = User.objects.get('-weapons_earned')
    # Get all weapons
    weapons_list = Weapon.objects.all()

    # Store user specific artifacts and weapons, with all artifacts and weapons into context dictionary 
    context_dict={}
    context_dict['user_artifacts'] = user_artifacts_list
    context_dict['artifacts'] = artifacts_list
    context_dict['user_weapons'] = user_weapons_list
    context_dict['weapons'] = weapons_list

    return render(request, 'gameApp/user_handbook.html', context=context_dict)


# Leaderboard view
# Visiblity: ALL users
# URL: gameApp/leaderboard/
# Template: gameApp/leaderboard.html
def leaderboard(request):

    # Get top 10 players with most kills
    player_enemies_list = User.objects.order_by('-most_enemies_killed')[:10] 
    # Get top 10 players with most days survived
    player_days_list = User.objects.order_by('-most_days_survived')[:10] 

    # Store player lists into context dictionary, to be used in html
    context_dict={}
    context_dict['player_enemies'] = player_enemies_list
    context_dict['player_days'] = player_days_list

    return render(request, 'gameApp/leaderboard.html', context=context_dict)


# Play view
# Visiblity: AUTHENTICATED users
# URL: gameApp/play/
# Template: gameApp/play.html
def play(request):
    context_dict={}
    return render(request, 'gameApp/play.html', context=context_dict)


# Game Scene view
# Visiblity: AUTHENTICATED users
# URL: gameApp/play/gameScene/
# Template: gameApp/gameScene.html
def gameScene(request):
    context_dict={}
    return render(request, 'gameApp/gameScene.html', context= context_dict)
