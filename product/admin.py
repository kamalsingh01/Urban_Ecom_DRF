from django.contrib import admin
from .models import Brand,Category,Product, ProductLine, ProductImage
from django.urls import reverse
from django.utils.safestring import mark_safe

# Register your models here.

#check InlineModeAdmin in djang.admin documentation


class EditLinkInLine(object):
    def edit(self, instance):
        #creating edit button using Admin Reverse URL section.
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args = [instance.pk],
        )
        if instance.pk:
            link = mark_safe('<a href="{u}">edit</a>'.format(u=url))
            return link
        else:
            return ""

class ProductLineImageInline(admin.TabularInline):
    model = ProductImage      

#enabling "Editing multiple models through Django Admin Site"
class ProductLineInline(EditLinkInLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]      
#mentioning admin that Productline model atrributes are also added with already existing attributes of product inside the Product form






class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductLineImageInline]   

admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin )
admin.site.register(Category)
admin.site.register(Brand)
