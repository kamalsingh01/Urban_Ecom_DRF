from pytest_factoryboy import register
from rest_framework.test import APIClient
import pytest
from .factories import CategoryFactory, BrandFactory, ProductFactory

register(CategoryFactory)
#this file is checked before any test file 
register(BrandFactory)
register(ProductFactory)

@pytest.fixture
def api_client():
    return APIClient