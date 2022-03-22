from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Products(models.Model):
    id=models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)


class Cart(models.Model):
    created_by= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    Prod_id=models.ManyToManyField(Products)

class Wishlist(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Prod_id = models.ManyToManyField(Products)