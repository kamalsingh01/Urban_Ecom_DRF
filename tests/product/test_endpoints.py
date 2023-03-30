import pytest
import factory
import json

pytestmark = pytest.mark.django_db

#we need to perform Migrations before performing the tests

class TestCategoryEndpoints:
    
    endpoint = "/api/category/"

    def test_category_get(self,category_factory, api_client):
        #Arrange
        category_factory.create_batch(4)
        #Act
        response = api_client().get(self.endpoint)
        #api_client here acts as a dummy client and sends the get request to endpoint and handles the response
        
        #Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        #assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    
    endpoint = "/api/brand/"

    def test_brand_get(self,brand_factory, api_client):
        #Arrange
        brand_factory.create_batch(3)
        #Act
        response = api_client().get(self.endpoint)
        #api_client here acts as a dummy client and sends the get request to endpoint and handles the response
        #Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        #assert len(json.loads(response.content)) == 3


class TestProductEndpoints:
    endpoint = "/api/product/"

    def test_return_all_products(self,product_factory, api_client):
        #Arrange
        product_factory.create_batch(2)
        #Act
        response = api_client().get(self.endpoint)
        #api_client here acts as a dummy client and sends the get request to endpoint and handles the response
        #Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        #assert len(json.loads(response.content)) == 2

    def test_return_single_product_by_name(self,product_factory, api_client):
        obj = product_factory(slug='test-slug')
        response = api_client().get(f"{self.endpoint}{obj.slug}/")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_return_product_by_category_slug(self, product_category, product_factory, api_client):
        # obj  = category_factory(slug="test-slug")
        # product_factory(category=obj)
        # response = api_client().get(f"{self.endpoint}{obj.slug}/")
        # assert response.status_code == 200
        # assert len(json.loads(response.content)) == 1
        pass
