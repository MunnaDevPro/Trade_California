from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['image_preview', 'is_featured', 'order']
    list_display_links = ['image_preview']
    list_editable = ['is_featured', 'order']
    list_filter = ['is_featured']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"

