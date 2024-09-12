from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'seller', 'color', 'product_dimensions')
    search_fields = ('name', 'seller', 'color')

admin.site.register(Product, ProductAdmin)
