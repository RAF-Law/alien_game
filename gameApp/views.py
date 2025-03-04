# View imports
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

# Authenication imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Model imports
# USER MODEL
# USERPROFILE MODEL



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
def login(request):
    context_dict={}
    return render(request, 'gameApp/login.html', context=context_dict)


# Logout
# Visiblity: AUTHENTICATED users
# URL: Null
# Template: Null
def logout(request):
    logout(request)
    return redirect(reverse('gameApp:index'))


# Player view
# Visiblity: AUTHENTICATED users
# URL: gameApp/player/
# Template: gameApp/player.html
def player(request):
    context_dict={}
    return render(request, 'gameApp/player.html', context=context_dict)


# Player History view
# Visiblity: AUTHENTICATED users
# URL: gameApp/player/player_history/
# Template: gameApp/player_history.html
def player_history(request):
    context_dict={}
    return render(request, 'gameApp/player_history.html', context=context_dict)


# Player Handbook view
# Visiblity: AUTHENTICATED users
# URL: gameApp/player/player_handbook/
# Template: gameApp/player_handbook.html
def player_handbook(request):
    context_dict={}
    return render(request, 'gameApp/player_handbook.html', context=context_dict)


# Leaderboard view
# Visiblity: ALL users
# URL: gameApp/leaderboard/
# Template: gameApp/leaderboard.html
def leaderboard(request):
    context_dict={}
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
