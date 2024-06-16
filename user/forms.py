from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2', 'sex','date_of_birth')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user
