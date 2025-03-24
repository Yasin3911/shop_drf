from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product

from .serializer import BrandSerializer, CategorySerializer, ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request):
        serializer_data = BrandSerializer(self.queryset, many=True)
        return Response(serializer_data.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        serializer_data = CategorySerializer(self.queryset, many=True)
        return Response(serializer_data.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        serializer_data = ProductSerializer(self.queryset, many=True)
        return Response(serializer_data.data)
