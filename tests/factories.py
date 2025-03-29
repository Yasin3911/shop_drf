import factory
from unicodedata import category

from product.models import Product, Brand, Category, ProductLine

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"category_test_{n}")

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f"brand_test_{n}")

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.sequence(lambda n: f"product_test_{n}")
    price = 100
    is_digital = False
    description = factory.sequence(lambda n: f"product_description_test_{n}")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    stock_qty = 10
    is_active = True
    sku = factory.sequence(lambda n: f"sku_{n}")
    price = 100
    product = factory.SubFactory(ProductFactory)