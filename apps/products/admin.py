from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, ProductImage
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

class ProductImageInline(TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'category', 'origin_country', 'is_featured']
    list_filter = ['category', 'is_featured', 'origin_country']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin):
    list_display = ['product', 'is_primary', 'image_preview']
    list_filter = ['is_primary']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"
