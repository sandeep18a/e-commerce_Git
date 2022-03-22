from rest_framework import serializers

from .models import Category, Products,Cart,Wishlist

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Products
       fields = ('id','name', 'price', 'category','description')

class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()
    class Meta:
        model=Cart
        fields=('created_by','Prod_id')

class WishListSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()
    class Meta:
        model=Wishlist
        fields=('created_by','Prod_id')