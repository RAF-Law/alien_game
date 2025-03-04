from django.contrib import admin
from .models import Weapon, Artifact, User, Game

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('weapon_id', 'name', 'attack_points', 'description')
    search_fields = ('name', 'description')

@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('artifact_id', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'player_hp', 'player_ap', 'player_speed', 'player_food', 'game_enemies_killed', 'game_day', 'game_difficulty', 'game_map')
