from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
# every model class represents a table in database. Class variables are fields/columns in DB


class Category(MPTTModel):
    name = models.CharField(max_length=100,unique=True)
    parent = TreeForeignKey("self",on_delete=models.PROTECT, null=True, blank=True)
    #to connect category to another sub category, like shoes under clothes/Apperals. Nested Categories
    #models.protect won't allow parent category to be deleted without deletion of child category.

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):   #to get a human redable output on admin
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):   #to get a human redable output on admin and 
        return self.name   #naming each tuple object returned in the Queryset using name attribute  

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    is_digital = models.BooleanField(default=False) #most products are shippable
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    #cascade, if we delete brand data in BRANMD table, the product also gets deleted.
    Category = TreeForeignKey("Category", on_delete=models.SET_NULL,null=True, blank = True)

    def __str__(self):   #to get a human redable outputon admin
        return self.name

#django automatically creates tables in Db with name as <app_name>_<class_name>