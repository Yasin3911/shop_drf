from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import BrandViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()

router.register('brand', BrandViewSet)
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
