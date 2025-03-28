from django import forms
from django.contrib.auth.models import User
from gameApp.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ #you can even have placeholders here wtf this is awesome
            'class': 'styled-input',
        }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'styled-input',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'styled-input',
            })
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('icon',)