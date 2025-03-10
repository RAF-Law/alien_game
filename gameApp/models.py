from django.db import models
from django.contrib.auth.models import User as DjangoUser


class Weapon(models.Model):

    # Primary key for weapon
    weapon_id = models.AutoField(primary_key=True)

    # Name of weapon
    name = models.CharField(max_length=100, unique=True)

    # Description of weapon
    description = models.TextField()

    # Attack points of weapon
    damage = models.IntegerField(default=0)

    # Attack message of weapon
    attack_message = models.CharField(max_length=100, blank=True)

    #Rarity of weapon
    rarity = models.IntegerField(default=1)

    # Icon of weapon
    icon = models.ImageField(upload_to='static/weapon_icons/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'


class Artifact(models.Model):
    # Primary key for artifact
    artifact_id = models.AutoField(primary_key=True)

    # Name of artifact
    name = models.CharField(max_length=100, unique=True)

    # Description of artifact
    description = models.TextField()

    # Rarity of artifact
    rarity = models.IntegerField(default=1)
    
    # Icon of artifact
    icon = models.ImageField(upload_to='static/artifact_icons/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artifact'
        verbose_name_plural = 'Artifacts'

class UserProfile(models.Model):

    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, primary_key=True)

    most_enemies_killed = models.IntegerField(default=0)
    most_days_survived = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    artifacts_earned = models.ManyToManyField(Artifact, blank=True)
    weapons_earned = models.ManyToManyField(Weapon, blank=True)

    def update_most_enemies_killed(self, current_game_enemies_killed):
        if current_game_enemies_killed > self.most_enemies_killed:
            self.most_enemies_killed = current_game_enemies_killed
            self.save()

    def update_most_days_survived(self, current_game_days_survived):
        if current_game_days_survived > self.most_days_survived:
            self.most_days_survived = current_game_days_survived
            self.save()

    def increment_games_played(self):
        self.games_played += 1
        self.save()

    def __str__(self):
        return f"User {self.user.username}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Game(models.Model):
    # Primary key for game (Map)
    game_id = models.AutoField(primary_key=True)

    # Player attributes
    player_hp = models.IntegerField(default=100)

    # Player attack points (ap)
    player_ap = models.IntegerField(default=10)

    # Player speed
    player_speed = models.IntegerField(default=5)

    # Player food
    player_food = models.IntegerField(default=10)

    # Player weapon
    player_weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True)

    # Enemies killed in current game instance
    game_enemies_killed = models.IntegerField(default=0)

    # Days survived in current game instance
    game_day = models.IntegerField(default=0)

    # Difficulty level of current game instance
    game_difficulty = models.IntegerField(default=1)

    # Current map of game instance (Starting at default map with PK of 1)
    game_map = models.IntegerField(default=1)

    def __str__(self):
        return f"Game {self.game_id}"

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
