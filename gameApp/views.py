# View imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

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
                return redirect(reverse("gameApp:home"))
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

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse('gameApp:user_account'))  # Reload page after updating PFP

    else:
        profile_form = UserProfileForm(instance=user_profile)

    # Pass form & user info to template
    context_dict = {'profile_form': profile_form, 'user_profile': user_profile}
    return render(request, 'gameApp/user_account.html', context=context_dict)



# User History view
# Visiblity: AUTHENTICATED users
# URL: gameApp/my_account/my_history/
# Template: gameApp/user_history.html
@login_required
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
@login_required
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
    context_dict={}
    return render(request, 'gameApp/gameScene.html', context= context_dict)

@login_required
def gameCreation(request):
    context_dict={}
    return render(request, 'gameApp/gameCreation.html', context= context_dict)

