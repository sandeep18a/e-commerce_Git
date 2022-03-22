from django.shortcuts import render

from rest_framework import viewsets,filters,generics

from ElecSales.serializers import CategorySerializer, ProductSerializer,CartSerializer,WishListSerializer
from ElecSales.models import Category, Products,Cart,Wishlist
from rest_framework import permissions



class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer


class ProductsViewSet(generics.ListCreateAPIView):
   search_fields= ['name']
   filter_backends = (filters.SearchFilter,)
   queryset = Products.objects.all()
   serializer_class = ProductSerializer

   def get_permissions(self):
      if self.request.method in ['POST']:
         return [permissions.IsAdminUser()]
      return [permissions.IsAuthenticated()]

class CartViewSet(generics.ListCreateAPIView):
   serializer_class=CartSerializer
   def get_queryset(self):
      username = self.kwargs['username']
      return Cart.objects.filter(created_by=username)
   # def get_permissions(self):
   #    if self.request.method in ['POST']:
   #       return [permissions.IsAdminUser()]
   #    return [permissions.IsAuthenticated()]


class WishListViewSet(generics.ListCreateAPIView):
   serializer_class=WishListSerializer
   def get_queryset(self):
      username = self.kwargs['username']
      return Wishlist.objects.filter(created_by=username)
   # def get_permissions(self):
   #    if self.request.method in ['POST']:
   #       return [permissions.IsAdminUser()]
   #    return [permissions.IsAuthenticated()]