from django.db import models
from registration.models import CustomUser


class Composition(models.Model):
    info = models.CharField(max_length=255)


class Size(models.Model):
    size = models.IntegerField()


class Color(models.Model):
    color = models.CharField(max_length=255)


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField(default='')
    quantity_per_unit = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    composition_id = models.ForeignKey(Composition, on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Review(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    rating = models.IntegerField()
    comment = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer_name}{self.email}{self.rating}{self.comment}{self.created_at}{self.product_id}'


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)


class Cart(models.Model):
    user = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateTimeField()
