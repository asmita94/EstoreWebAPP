from django.contrib import admin
from .models import Product
from .models import Product2

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pdetails', 'cate']
    list_filter=['cate','is_active']

admin.site.register(Product, ProductAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price','pdetails', 'cate']
    list_filter=['cate','is_active']

admin.site.register(Product2,ProductAdmin)

