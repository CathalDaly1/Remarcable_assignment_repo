from django.contrib import admin
from .models import Product, Category, Tag

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for Product model."""
    
    # Fields to display in the admin list view
    list_display = ('name', 'category', 'price', 'created_at')
    
    # Fields to use as filters in the admin sidebar
    list_filter = ('category', 'tags')
    
    # Fields to search against in the admin search box
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model."""
    
    # Fields to display in the admin list view (tuple with single item)
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin configuration for Tag model."""
    
    # Fields to display in the admin list view (tuple with single item)
    list_display = ('name',)
