import os
from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.db.models.signals import post_save
from django.core.files.base import File

class Weapon(models.Model):

    weapon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    damage = models.IntegerField(default=0)
    attack_message = models.CharField(max_length=100, blank=True)
    rarity = models.IntegerField(default=1)
    icon = models.ImageField(upload_to='static/weapon_icons/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'

class Artifact(models.Model):

    artifact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    rarity = models.IntegerField(default=1)
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
    history_games = models.JSONField(default=list)

    icon = models.ImageField(upload_to='static/user_icons/', blank=True, default =
    File(open('static/user_icons/Default Icon.png', 'rb')))

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
        return self.user.username
    
    def save(self, *args, **kwargs): #delete old pfp when uploading a new one
        if self.pk:
            existing = UserProfile.objects.filter(pk=self.pk).first()
            if existing and existing.icon and self.icon != existing.icon:
                if os.path.isfile(existing.icon.path):
                    os.remove(existing.icon.path)

        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def create_user_game(sender, instance, created, **kwargs):
    if created:
        Game.objects.create(user_game=instance)

class Game(models.Model):

    user_game = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, primary_key=True)
    game_data = models.TextField(blank=True)

    # ^^ I'm actually thinking whether we can just store raw xml text data to database without any parsing
    # so we just need one textfield above, no need to seperate details out
    # when we load from database we throw it back to js and let it handle
    # but then we need to modify the save_history view to let it update the artifacts/weapons user has found
    # whatever you choose to implement please make sure it correctly updates the artifacts/weapons the user found & the game data is not lost

    # up to you tho, feel free to choose a way you like
    # also feel free to ask if you're unsure about the code or workflow :p

    def __str__(self):
         return f"Game for {self.user_game.username}"

post_save.connect(create_user_profile, sender=DjangoUser)
post_save.connect(create_user_game, sender=DjangoUser)

#https://docs.djangoproject.com/en/5.1/ref/signals/ - Really useful stuff