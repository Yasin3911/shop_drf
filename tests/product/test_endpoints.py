import json
import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:

    endpoint = '/api/category/'

    def test_get_category(self, category_factory, client):

        category_factory.create_batch(4)

        response = client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_bad_get_category(self, category_factory, client):

        category_factory()

        response = client().get(self.endpoint + "nothing/")

        assert response.status_code == 404

    def test_redirect_bad_get_category(self, category_factory, client):

        category_factory()

        response = client().get(self.endpoint + "nothing")

        assert response.status_code == 301

class TestBrandEndpoints:

    endpoint = '/api/brand/'

    def test_get_brand(self, brand_factory, client):

        brand_factory.create_batch(4)

        response = client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_bad_get_brand(self, brand_factory, client):

        brand_factory()

        response = client().get(self.endpoint + "nothing/")

        assert response.status_code == 404

    def test_redirect_bad_get_brand(self, brand_factory, client):

        brand_factory()

        response = client().get(self.endpoint + "nothing")

        assert response.status_code == 301

class TestProductEndpoints:

    endpoint = '/api/product/'

    def test_get_all_product(self, product_factory, client):

        product_factory.create_batch(4)

        response = client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_get_product(self, product_factory, client):

        obj = product_factory(name='test_product')

        response = client().get(f"{self.endpoint}{obj.id}/")

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 7

    def test_get_product_with_category(self, product_factory, category_factory, client):
        obj = category_factory(name='test_category')
        product_factory(category=obj)
        product_factory(category=obj)
        product_factory()
        response = client().get(f"{self.endpoint}category/{obj.name}/")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_get_product_with_brand(self, product_factory, brand_factory, client):
        obj = brand_factory(name='test_brand')
        product_factory(brand=obj)
        product_factory(brand=obj)
        product_factory(brand=obj)
        product_factory()
        response = client().get(f"{self.endpoint}brand/{obj.name}/")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_bad_get_product(self, product_factory, client):

        product_factory()

        response = client().get(self.endpoint + "nothing/")

        assert response.status_code == 400

    def test_redirect_bad_get_product(self, product_factory, client):

        product_factory()

        response = client().get(self.endpoint + "nothing")

        assert response.status_code == 301
