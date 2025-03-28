from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

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

class ProductViewSet(viewsets.ViewSet):
    # queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.isActive()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer_data = ProductSerializer(self.get_queryset(), many=True)
        return Response(serializer_data.data)

    def retrieve(self, request, pk=None):
        # serializer_data = ProductSerializer(self.queryset.get(pk=pk))
        if pk.isdigit() == False:
            return Response({'message': 'Product ID is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer_data = ProductSerializer(get_object_or_404(self.get_queryset(), pk=pk))

        return Response(serializer_data.data)

    @extend_schema(responses=ProductSerializer, request=ProductSerializer)
    def create(self, request):
        serializer_data = ProductSerializer(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=ProductSerializer, request=ProductSerializer)
    def update(self, request, pk=None):
        if pk.isdigit() == False:
            return Response({'message': 'Product ID is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(self.get_queryset(), pk=pk)
        serializer_data = ProductSerializer(product, data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=ProductSerializer, request=ProductSerializer)
    def partial_update(self, request, pk=None):
        if pk.isdigit() == False:
            return Response({'message': 'Product ID is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(self.get_queryset(), pk=pk)
        serializer_data = ProductSerializer(product, data=request.data, partial=True)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=None)
    def destroy(self, request, pk=None):
        if pk.isdigit() == False:
            return Response({'message': 'Product ID is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(self.get_queryset(), pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, url_path="category/(?P<category>.+)")
    def get_list_with_category_filter(self, request, category=None):
        serializer_data = ProductSerializer(self.get_queryset().filter(category__name=category), many=True)
        return Response(serializer_data.data)

    @action(methods=['get'], detail=False, url_path="brand/(?P<brand>.+)")
    def get_list_with_brand_filter(self, request, brand=None):
        serializer_data = ProductSerializer(self.get_queryset().filter(brand__name=brand), many=True)
        return Response(serializer_data.data)
