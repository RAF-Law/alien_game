from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

import os
from .models import Weapon, Artifact, UserProfile, Game

class WeaponModelTest(TestCase):

    def setUp(self):

        self.weapon = Weapon.objects.create(
            name="Test Weapon",
            description="A Test Weapon",
            damage=999,
            attack_message="Test attack message",
            rarity=999
        )

    def test_weapon_creation(self):

        self.assertEqual(self.weapon.name, "Test Weapon")
        self.assertEqual(self.weapon.damage, 999)
        self.assertEqual(self.weapon.rarity, 999)
        self.assertEqual(str(self.weapon), "Test Weapon")

    def test_weapon_icon_upload(self):

        test_icon = SimpleUploadedFile(
            "test_weapon.png",
            b"file_content",
            content_type="image/png"
        )
        self.weapon.icon = test_icon
        self.weapon.save()

        self.assertTrue(self.weapon.icon.name.startswith('static/weapon_icons/'))

        if os.path.exists(self.weapon.icon.path):
            os.remove(self.weapon.icon.path)

class ArtifactModelTest(TestCase):

    def setUp(self):

        self.artifact = Artifact.objects.create(
            name="Test Artifact",
            description="A Test Artifact",
            rarity=999
        )

    def test_creation(self):

        self.assertEqual(self.artifact.name, "Test Artifact")
        self.assertEqual(self.artifact.rarity, 999)
        self.assertEqual(str(self.artifact), "Test Artifact")

    def test_icon_upload(self):

        test_icon = SimpleUploadedFile(
            "test_artifact.png",
            b"file_content",
            content_type="image/png"
        )

        self.artifact.icon = test_icon
        self.artifact.save()
        self.assertTrue(self.artifact.icon.name.startswith('static/artifact_icons/'))

        if os.path.exists(self.artifact.icon.path):
            os.remove(self.artifact.icon.path)

class UserProfileModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='test_user_TEST',
            password='123'
        )

        self.profile = UserProfile.objects.get(user=self.user)

    

    def test_creation(self):

        self.assertEqual(self.profile.user.username, 'test_user_TEST')
        self.assertEqual(self.profile.most_enemies_killed, 0)
        self.assertEqual(self.profile.most_days_survived, 0)
        self.assertEqual(str(self.profile), 'test_user_TEST')

    def test_stats_update(self):

        self.profile.update_most_enemies_killed(1)
        self.assertEqual(self.profile.most_enemies_killed, 1)
        
        self.profile.update_most_days_survived(1)
        self.assertEqual(self.profile.most_days_survived, 1)
        
        self.profile.increment_games_played()
        self.assertEqual(self.profile.games_played, 1)

    def test_icon_update(self):

        test_icon = SimpleUploadedFile(
            "test_icon.png",
            b"file_content",
            content_type="image/png"
        )

        old_icon_path = self.profile.icon.path
        
        self.profile.icon = test_icon
        self.profile.save()
        
        self.assertTrue(self.profile.icon.name.startswith('static/user_icons/'))
        self.assertFalse(os.path.exists(old_icon_path))
        
        if os.path.exists(self.profile.icon.path):
            os.remove(self.profile.icon.path)

    def test_artifacts_relationship(self):

        artifact = Artifact.objects.create(
            name="Test Artifact",
            description="Test",
            rarity=1
        )

        self.profile.artifacts_earned.add(artifact)
        self.assertEqual(self.profile.artifacts_earned.count(), 1)

    def test_weapons_relationship(self):

        weapon = Weapon.objects.create(
            name="Test Weapon",
            description="Test",
            damage=5,
            rarity=1
        )

        self.profile.weapons_earned.add(weapon)
        self.assertEqual(self.profile.weapons_earned.count(), 1)

class GameModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='test_game',
            password='123'
        )

        self.game = Game.objects.get(user_game=self.user)

    def test_creation(self):

        self.assertEqual(self.game.user_game.username, 'test_game')
        self.assertEqual(self.game.game_data, '')
        self.assertEqual(str(self.game), f"Game for {self.user.username}")

    def test_data_storage(self):

        test_data = "<game><player><health>20</health></player></game>"

        self.game.game_data = test_data
        self.game.save()
        
        updated_game = Game.objects.get(pk=self.game.pk)

        self.assertEqual(updated_game.game_data, test_data)

class SignalTests(TestCase):

    def test_user_profile_creation(self):

        user = User.objects.create_user(
            username='test_userProfile',
            password='123'
        )

        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_game_creation(self):

        user = User.objects.create_user(
            username='test_game',
            password='123'
        )

        self.assertTrue(Game.objects.filter(user_game=user).exists())

class UserAuthTests(TestCase):

    def test_wrong_password(self):

        user = User.objects.create_user(
            username='test_user',
            password='123'
        )

        self.assertTrue(user.check_password('123'))
        self.assertFalse(user.check_password('wrong_password'))

    def test_superuser_creation(self):

        superuser = User.objects.create_superuser(
            username='test_admin_TEST',
            password='123'
        )

        self.assertTrue(User.objects.filter(username='test_admin_TEST').exists())
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class DefaultViewTests(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('gameApp:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gameApp/home.html')

    def test_instructions_view(self):
        response = self.client.get(reverse('gameApp:instructions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gameApp/instructions.html')

    def test_leaderboard_view(self):
        response = self.client.get(reverse('gameApp:leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gameApp/leaderboard.html')
        self.assertIn('player_enemies', response.context)
        self.assertIn('player_days', response.context)

    def test_restricted_view(self):
        response = self.client.get(reverse('gameApp:gameScene'))
        self.assertEqual(response.status_code, 302)

class AuthViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_register_view(self):
        response = self.client.get(reverse('gameApp:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gameApp/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('gameApp:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gameApp/login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('gameApp:logout'))
        self.assertEqual(response.status_code, 302)

    def test_restricted_admin_view(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

