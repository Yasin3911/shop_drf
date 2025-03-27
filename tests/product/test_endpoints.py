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

    def test_get_product(self, product_factory, client):

        product_factory.create_batch(4)

        response = client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_bad_get_product(self, product_factory, client):

        product_factory()

        response = client().get(self.endpoint + "nothing/")

        assert response.status_code == 404

    def test_redirect_bad_get_product(self, product_factory, client):

        product_factory()

        response = client().get(self.endpoint + "nothing")

        assert response.status_code == 301
