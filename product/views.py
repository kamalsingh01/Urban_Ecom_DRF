from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer,BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from django.db import connection

#Viewsets are class based views
#Using viewsets allows us to use combined repeatable logics in a single class.
#Secondly, compatible with routers
#in Viewset class, we combine mutiple functions and create multiple coresponding endpoints from within one class
#Viewset also allows us to choose between type of functions/actions we need 
#Wheres ModelViewSet which inhertits GenericAPIView by default provides all the actions all at once.(no choice)

#sometimes default actions provided by viewset isn't enough, so add extra actions within the class enbling better formatting & display of endpoints
#Preferred to choose a systematic and easy to read naming schemes of the endpoints.
# Also it is preferred not to use primary key as filter due to security resons. it may give some non-required information to the user and also while scrapping
#So better to use names associated to PK
# for names with gaps/dash in between we use 'slug' which isa way of creating usable URLs and utilized and requests and uRLS. slug is passed to the views.

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    '''
    A simple viewset for viewing categories
    ''' 
    queryset = Category.objects.all()
    #we can define queryset once and can use it with all methods under the same class
    
    serializer_class = CategorySerializer

    @extend_schema(responses=CategorySerializer)
    def list(self,request): #defining how we are returning the data to client
        serializer = CategorySerializer(self.queryset,many=True)
        return  Response(serializer.data)    

class BrandViewSet(viewsets.ViewSet):
    '''
    A simple viewset for viewing Brands
    ''' 
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    #print(queryset)
    

    @extend_schema(responses=BrandSerializer)
    def list(self,request): #defining how we are returning the data to client
        serializer = BrandSerializer(self.queryset,many=True)
        return  Response(serializer.data)  
    
class ProductViewSet(viewsets.ViewSet):
    '''
    A simple viewset for viewing Products
    ''' 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    #print(queryset)
        
    def retrieve(self,request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug),many=True)
        data = Response(serializer.data)
        #q = list(connection.queries)
        #print(len(q))
        return data

    @extend_schema(responses=ProductSerializer)
    def list(self,request): #defining how we are returning the data to client
        serializer = ProductSerializer(self.queryset,many=True)
        #many=True, means views are sending multiple objects
        return  Response(serializer.data)  
    
    @action( methods= ["get"], 
            detail=False,   #disabling automatic filter procedure and creating our own type of filter
            url_path=r"Category/(?P<Category>\w+)/all", # this url segmnent is added after the product endpoint URL
    )
    def list_product_by_category(self,request, Category=None):  
    #'category' because we need to strip requested category from URL and use that to create a new queryset of requested object.
        '''
        An endpoint to return product based on category
        ''' 
        serializer = ProductSerializer(self.queryset.filter(Category__name = Category),many=True)
        #many=True, means views are sending multiple objects
        return  Response(serializer.data)  
    
