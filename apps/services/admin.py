from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ServiceType

@admin.register(ServiceType)
class ServiceTypeAdmin(ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
