from django.contrib import admin

from .models import Category, Product, ProductImage


#TODO: Реализовать загрузку нескольких изображений
class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    # readonly_fields = ['image',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['name', 'description']
    inlines = [ProductImageInLine]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

