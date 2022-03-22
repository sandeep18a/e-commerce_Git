from django.urls import include, path
from rest_framework import routers
from ElecSales.views import ProductsViewSet,CategoryViewSet,CartViewSet

router = routers.DefaultRouter()
# router.register(r'Products', ProductsViewSet)
router.register(r'Category', CategoryViewSet)
# router.register(r'Cart', CartViewSet)

urlpatterns = [
   path('', include(router.urls))
]