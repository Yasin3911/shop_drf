import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        new_object = category_factory(name = "category_test")
        assert new_object.__str__() == "category_test"

class TestBrandModel:
    def test_str_method(self, brand_factory):
        new_object = brand_factory(name = "brand_test")
        assert new_object.__str__() == "brand_test"

class TestProductModel:
    def test_str_method(self, product_factory):
        new_object = product_factory(name = "product_test")
        assert new_object.__str__() == "product_test"

class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        new_object = product_line_factory(sku = "sku_test")
        assert new_object.__str__() == "sku_test"

    def test_duplicate_order(self, product_line_factory, product_factory):
        prd = product_factory()
        product_line_factory(order=1, product=prd)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=prd).clean_fields(None)