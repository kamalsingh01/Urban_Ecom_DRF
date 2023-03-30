import factory 

from product.models import Category,Brand,Product,ProductLine

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        #we need to define fields which needs to populate

    name = factory.Sequence(lambda n: "Category_%d" % n)
    #name  = "test_category" - this won't work as Unique=True in C bategory.name
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        #we need to define fields which needs to populate

    name = factory.Sequence(lambda n: "Brand_%d" % n)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = Product

    name = "test_product"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    Category = factory.SubFactory(CategoryFactory)
    is_active = True

class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = ProductLine

    price = 10.00
    sku = "12345"
    stock_qty = 1
    product = factory.SubFactory(ProductFactory)
    is_active = True