from django.contrib import admin
from unfold.admin import ModelAdmin
from solo.admin import SingletonModelAdmin
from .models import SiteSettings, NavigationLink, FooterLink, CompanyValue, Mentor

@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin, ModelAdmin):
    pass

@admin.register(NavigationLink)
class NavigationLinkAdmin(ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['label', 'url']

@admin.register(FooterLink)
class FooterLinkAdmin(ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['label', 'url']

@admin.register(CompanyValue)
class CompanyValueAdmin(ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title']

@admin.register(Mentor)
class MentorAdmin(ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'role']
