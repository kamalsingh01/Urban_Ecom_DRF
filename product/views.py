from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer,BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    '''
    A simple viewset for viewing categories
    ''' 
    queryset = Category.objects.all()
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
    #print(queryset)

    @extend_schema(responses=ProductSerializer)
    def list(self,request): #defining how we are returning the data to client
        serializer = ProductSerializer(self.queryset,many=True)
        #many=True, means views are sending multiple objects
        return  Response(serializer.data)  