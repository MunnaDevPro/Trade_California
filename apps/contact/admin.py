from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import OfficeLocation, ContactMessage

@admin.register(OfficeLocation)
class OfficeLocationAdmin(ModelAdmin):
    list_display = ["name", "phone", "order"]
    list_editable = ["order"]

@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ["name", "phone", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["name", "phone", "message"]
    readonly_fields = ["name", "phone", "message", "created_at"]
