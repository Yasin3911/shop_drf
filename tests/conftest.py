import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from factories import CategoryFactory, BrandFactory, ProductFactory


register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

@pytest.fixture
def client():
    return APIClient