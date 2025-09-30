from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'is_available', 'created_date')
    list_filter = ('category', 'is_available')
    search_fields = ('product_name', 'category__category_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

