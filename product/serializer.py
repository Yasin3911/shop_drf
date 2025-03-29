from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine


class BrandSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='name')

    class Meta:
        model = Brand
        fields = ['brand_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']

class ProductLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductLine
        exclude = ['id', 'product', 'is_active']

class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    # category = CategorySerializer()
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'brand_name',
            'category_name',
            'product_line',
            'description',
            'price',
            'is_digital',
        ]

    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        category_data = validated_data.pop('category')
        product_lines_data = validated_data.pop('product_line')

        brand, created = Brand.objects.get_or_create(name=brand_data['name'])
        category, created = Category.objects.get_or_create(name=category_data['name'])

        product = Product.objects.create(brand=brand, category=category, **validated_data)

        for pld in product_lines_data:
            ProductLine.objects.create(product=product, **pld)

        return product

    def update(self, instance, validated_data):
        brand_data = validated_data.get('brand', None)
        if brand_data:
            brand, created = Brand.objects.get_or_create(name=brand_data['name'])
            instance.brand = brand

        category_data = validated_data.get('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            instance.category = category

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.is_digital = validated_data.get('is_digital', instance.is_digital)

        product_lines_data = validated_data.get('product_line', None)
        if product_lines_data:
            self.update_product_lines(instance, product_lines_data)
            # instance.product_line.all().delete()
            # for pld in product_lines_data:
            #     ProductLine.objects.create(product=instance, **pld)

        instance.save()
        return instance

    def update_product_lines(self, product_instance, product_lines_data):
        existing_product_lines = {obj.sku: obj for obj in product_instance.product_line.all()}

        for product_line in product_lines_data:
            sku = product_line['sku']
            if sku in existing_product_lines:
                line = existing_product_lines[sku]
                for attr, value in product_line.items():
                    setattr(line, attr, value)
                line.save()
                existing_product_lines.pop(sku)
            else:
                product_instance.product_line.create(**product_line)

        for product_line in existing_product_lines.values():
            product_line.delete()
