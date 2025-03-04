from django.urls import path
from gameApp import views

app_name = 'gameApp'

urlpatterns = [
    path('', views.home, name='home'),
]
