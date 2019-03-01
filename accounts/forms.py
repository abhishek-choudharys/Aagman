from django import forms
from django.db import transaction
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ('username', 'name', 'email', 'number', 'address')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user




class StartupSignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ('username', 'name', 'email', 'number', 'address','dipp','description')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_startup = True
        user.save()
        return user