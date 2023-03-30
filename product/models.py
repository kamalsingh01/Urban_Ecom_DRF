from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField
from django.core.exceptions import ValidationError

#Class for Model Manager
class ActiveQuerySet(models.QuerySet):
    #we can override querysets for custom product filtering
    def isactive(self):
        return self.filter(is_active=True)  #filterig out product which is active from queryset
    
    

# Create your models here.
# every model class represents a table in database. Class variables are fields/columns in DB
#django automatically creates tables in Db with name as <app_name>_<class_name>

class Category(MPTTModel):
    name = models.CharField(max_length=100,unique=True)
    parent = TreeForeignKey("self",on_delete=models.PROTECT, null=True, blank=True)
    #to connect category to another sub category, like shoes under clothes/Apperals. Nested Categories
    #models.protect won't allow parent category to be deleted without deletion of child category.
    is_active = models.BooleanField(default=False)

    objects = ActiveQuerySet.as_manager()

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):   #to get a human redable output on admin
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(default=False)

    objects = ActiveQuerySet.as_manager()

    def __str__(self):   #to get a human redable output on admin and 
        return self.name   #naming each tuple object returned in the Queryset using name attribute  

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank = True)
    is_digital = models.BooleanField(default=False) #most products are shippable
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    #cascade, if we delete brand data in BRANMD table, the product also gets deleted.
    Category = TreeForeignKey("Category", on_delete=models.SET_NULL,null=True, blank = True)
    is_active = models.BooleanField(default=False)

    #objects = ActiveManager()
    #isactive = Activemanager()
    objects = ActiveQuerySet.as_manager()


    def __str__(self):   #to get a human redable outputon admin
        return self.name

#One Product can have multiple product line, i.e. multiple colors and sizes
class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku  = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line") 
        # related_name is used to enable reverse relationship amon models in serializers
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field ="product", blank=True) 
    # blank makes sure we need not to supply any data manually cuz it will be automatically get populated from fields.py(OrderField())
    #unique_for_field defines that Ordering is done on the basis of the product information and the product, product lines are assciated to, 
    # so ordering will be related to a subproduct being connected to a product.
    objects = ActiveQuerySet.as_manager()

    def clean(self, exclude = None):
        #super().clean_fields(exclude=exclude)
        qs = ProductLine.objects.filter(product = self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value")

    def __str__(self):
        return str(self.sku)
    
#Product Image Model
class ProductImage(models.Model):
    #name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default = "test.jpg")  #using pillow for imagefield
    product_line = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name="product_image")
    order = OrderField(unique_for_field ="product_line", blank=True) 

    def clean(self, exclude = None):
        #super().clean_fields(exclude=exclude)
        qs = ProductImage.objects.filter(product_line = self.product_line)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value")
            
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.url)

#Product Image Model - by Very Academy
# class ProductImage(models.Model):
#     alternative_text = models.CharField(max_length=100)
#     url = models.ImageField(upload_to=None, default="test.jpg")
#     product_line = models.ForeignKey(
#         ProductLine, on_delete=models.CASCADE, related_name="product_image"
#     )
#     order = OrderField(unique_for_field="product_line", blank=True)

#     def clean(self):
#         qs = ProductImage.objects.filter(product_line=self.product_line)
#         for obj in qs:
#             if self.id != obj.id and self.order == obj.order:
#                 raise ValidationError("Duplicate value.")

#     def save(self, *args, **kwargs):
#         self.full_clean()
#         return super(ProductImage, self).save(*args, **kwargs)

#     def __str__(self):
#         return str(self.order)