from rest_framework import serializers

from .models import Category, Product, Brand, ProductLine, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    #serializer field name mapping
    category_name = serializers.CharField(source='name')
    
    class Meta:
        model = Category
        fields = ["category_name"] #used to get name only
        

class BrandSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='name')
    class Meta:
        model = Brand
        #fields = "__all__" - included all the fields
        #exclude = ("id",)
        fields = ["brand_name"]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id","product_line",)

class ProductLineSerializer(serializers.ModelSerializer):
    product_image= ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        #fields = "__all__"
        fields = [
            "price",
            "sku",
            "stock_qty",
            "order",
            "product_image"
        ]

class ProductSerializer(serializers.ModelSerializer):
    #fetching data from Brand & Category table to product table
    #because we are using Brand data as foriegn key in product so that
    #brand data also needs to be serialized,
    brand_name = serializers.CharField(source="brand.name")  #called Flattening
    Category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)  #Reverse relationhship in serializers

    class Meta:
        model = Product
        #fields = "__all__"
        #exclude = ("id",)
        fields = ("name",
                  "slug",
                  "description",
                  "brand_name",
                  "Category",
                  "product_line",
        )

