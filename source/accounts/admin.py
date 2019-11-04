from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Team


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['birth_date', 'avatar']


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline]



class TeamAdmin(admin.ModelAdmin):
    fields = ['user_key', 'project_key','started_at','finished_at']
    list_display = ['user_key', 'project_key','started_at','finished_at']
    list_filter = ['project_key']


admin.site.register(Team, TeamAdmin)
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)