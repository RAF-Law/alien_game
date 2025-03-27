from django.contrib import admin
from .models import Weapon, Artifact, UserProfile, Game

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('weapon_id', 'name', 'damage', 'rarity')
    list_filter = ('rarity',)
    search_fields = ('name', 'description')
    readonly_fields = ('weapon_id',)

@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('artifact_id', 'name', 'rarity')
    list_filter = ('rarity',)
    search_fields = ('name', 'description')
    readonly_fields = ('artifact_id',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'most_enemies_killed', 'most_days_survived', 'games_played')
    filter_horizontal = ('artifacts_earned', 'weapons_earned')
    search_fields = ('user__username',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('user_game', 'truncated_game_data')
    list_filter = ('user_game__username',)
    search_fields = ('user_game__username',)
    readonly_fields = ('user_game', 'get_game_data_preview')
    
    def truncated_game_data(self, obj):
        if obj.game_data:
            return obj.game_data[:100] + '...' if len(obj.game_data) > 100 else obj.game_data
        return "No game data"
    truncated_game_data.short_description = 'Game Data (Preview)'
    
    def get_game_data_preview(self, obj):
        if obj.game_data:
            return f'<textarea style="width:100%; height:300px;" readonly>{obj.game_data}</textarea>'
        return "No game data"
    get_game_data_preview.allow_tags = True
    get_game_data_preview.short_description = 'Full Game Data'