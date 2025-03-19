from django.urls import path
from gameApp import views

app_name = 'gameApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('instructions/', views.instructions, name='instructions'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_account/', views.user_account, name='user_account'),
    path('user_account/my_history/', views.user_history, name='user_history'),
    path('user_account/my_handbook/', views.user_handbook, name='user_handbook'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('play/', views.play, name='play'),
    path('play/gameScene/', views.gameScene, name='gameScene'),
    path('play/gameCreation/', views.gameCreation, name='gameCreation'),
]
