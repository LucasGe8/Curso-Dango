from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'discount_until')
    search_fields = ('name', 'description')
    list_filter = ('stock', 'discount_until')
    ordering = ('name',)    
    date_hierarchy = 'discount_until'
admin.site.register(Product, ProductAdmin)
