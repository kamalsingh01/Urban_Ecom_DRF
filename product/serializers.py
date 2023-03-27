from rest_framework import serializers

from .models import Category, Product, Brand

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["name"]

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    #fetching data from Brand & Category table to product table
    #because we are using Brand data as foriegn key in product so that
    #brand data also needs to be serialized,
    brand = BrandSerializer()
    Category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


