from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created_at', 'modified']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
