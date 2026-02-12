from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ユーザー名', 'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'パスワード', 'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'パスワード確認', 'class': 'form-input'}),
        }
