from django.urls import path
from gameApp import views

app_name = 'gameApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('instructions/', views.instructions, name='instructions'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('player/', views.player, name='player'),
    path('player/player_history/', views.player_history, name='player_history'),
    path('player/player_handbook/', views.player_handbook, name='player_handbook'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('play/', views.play, name='play'),
    path('play/gameScene/', views.gameScene, name='gameScene'),
]