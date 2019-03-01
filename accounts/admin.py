from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomerSignUpForm,StartupSignUpForm

class CustomUserAdmin(UserAdmin):
    form = CustomerSignUpForm
    add_form = StartupSignUpForm
    list_display = ('username', 'name', 'email', 'number', 'address','is_customer','dipp','description','is_startup','picture')
    model =CustomUser

admin.site.register(CustomUser,CustomUserAdmin)
