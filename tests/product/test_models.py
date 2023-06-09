#unit test
#whenever unit testing is performed, pytest automatically creates a temporary database
#with the data which we already have(replica of real DB) but initially it is empty and we need 
#to populate it with data to test
# using factory module, the data gets automatially pre-populated to be bact and asserted.
import pytest
from django.core.exceptions import ValidationError


pytestmark = pytest.mark.django_db   #for allowing db access to all tests

class TestCategoryModels:
    def test_str_method(self,category_factory):
        # Test Stages(AAA): 
        # ->Arrange(gathering resources and isolating the code for test) 
        
        # -> Act (utilising the code we are testing)
        obj = category_factory(name = "test_cat")
        # -> Assert(testing real outcome v/s expected ), returns boolean values
        assert obj.__str__() == "test_cat"

class TestBrandModels:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory(name="test_brand")
        #Assert
        assert obj.__str__() == "test_brand"

class TestProductModels:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name="test_product")
        #Assert
        assert obj.__str__() == "test_product"


class TestProductLineModels:
    def test_str_method(self,product_line_factory):
        obj = product_line_factory(sku='12345')
        assert obj.__str__() == "12345"

    def test_duplicate_order_values(self, product_line_factory,product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()