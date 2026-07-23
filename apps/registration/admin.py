from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import RegistrationRequest

@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(ModelAdmin):
    list_display = ["full_name", "company_name", "role", "status", "created_at"]
    list_filter = ["status", "role", "created_at"]
    search_fields = ["full_name", "company_name", "email"]
    readonly_fields = ["full_name", "company_name", "email", "phone", "country", "role", "message", "created_at"]
