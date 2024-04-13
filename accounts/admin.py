from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'name', 'is_staff', 'is_superuser']

    fieldset = UserAdmin.fieldsets + ((None, {'fields': ('name',)}),)
    add_fieldset = UserAdmin.add_fieldsets + ((None, {'fields': ('name',)}),)

admin.site.register(CustomUser, CustomUserAdmin)