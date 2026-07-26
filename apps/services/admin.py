from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ServiceType, FAQ

@admin.register(ServiceType)
class ServiceTypeAdmin(ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ['question', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['question', 'answer']
