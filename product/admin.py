from django.contrib import admin
from .models import Brand,Category,Product, ProductLine
# Register your models here.

#check InlineModeAdmin in djang.admin documentation

#enabling "Editing multiple models through Django Admin Site"
class ProductLineInline(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]      
#mentioning admin that Productline model atrributes are also added with already existing attributes of product inside the Product form

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)