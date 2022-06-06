from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegister(UserCreationForm):
    age = forms.IntegerField()
    email = forms.EmailField()
    # Country =  forms.CharField(max_length=30)
    # State = forms.CharField(max_length=30)
    # religion_choices = {
    #     ("Any", "Any"),
    #     ("Hindu", "Hindu"),
    #     ("Christian", "Christian"),
    #     ("Muslim", "Muslim"),
    #     ("Sikh", "Sikh"),
    #     ("Jain", "Jain"),
    #     ("Buddhist", "Buddhist"),
    # }
    # religion = forms.ChoiceField(choices=religion_choices)

    class Meta:
        model = User
        fields = ["username", "email", "age", "password1", "password2"]


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "Country",
            "State",
            "age",
            "religion",
            "usersocialTWT",
            "usersocialINSTA",
            "usersocialFB",
        ]
