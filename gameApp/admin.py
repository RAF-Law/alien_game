from django.contrib import admin
from .models import Weapon, Artifact, UserProfile, Game

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('weapon_id', 'name', 'damage', 'description', 'attack_message', 'rarity', 'icon')
    list_filter = ('rarity',)
    search_fields = ('name', 'description', 'attack_message')
    readonly_fields = ('weapon_id',)

@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('artifact_id', 'name', 'description', 'rarity', 'icon')
    list_filter = ('rarity',)
    search_fields = ('name', 'description')
    readonly_fields = ('artifact_id',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'most_enemies_killed', 'most_days_survived', 'games_played', 'icon')
    filter_horizontal = ('artifacts_earned', 'weapons_earned')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('user_game', 'player_hp', 'player_ap', 'player_speed', 'player_food', 'player_weapon', 'game_enemies_killed', 'game_day', 'game_difficulty', 'game_map')
    list_filter = ('game_difficulty', 'game_map')
    search_fields = ('user_game', 'player_weapon__name')
    readonly_fields = ('user_game',)
