# Generated by Django 5.1.6 on 2025-03-07 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameApp', '0003_userprofile_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
