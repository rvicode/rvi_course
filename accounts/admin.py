from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'Description', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('Description', 'image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('Description', 'image')}),
    )
