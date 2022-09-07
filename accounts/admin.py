from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'phone', 'date_created', 'is_team_member', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'phone', 'description', 'profile_pic', 'is_teacher', 'is_team_member', 'instagram', 'whatsapp', 'telegram',
            'facebook', 'twitter', 'reddit', 'github', 'linkedin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
        'phone', 'description', 'profile_pic', 'is_teacher', 'is_team_member', 'instagram', 'whatsapp', 'telegram',
        'facebook', 'twitter', 'reddit', 'github', 'linkedin')}),
    )
