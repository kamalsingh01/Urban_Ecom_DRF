from django.contrib import admin
from django.urls import include, path
from product.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"category",CategoryViewSet)

urlpatterns = [
    path('',include(router.urls)),
]