from turtle import textinput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
import authentication.models as models


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name")


class FollowUsersForm(forms.Form):
    username = forms.CharField()
