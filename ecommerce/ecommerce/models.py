from django.db import models


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
    composition_id = models.ForeignKey(Composition)
    size_id = models.ForeignKey(Size)
    color_id = models.ForeignKey(Color)
    brand_id = models.ForeignKey(Brand)


class Review(models.Model):
    rating = models.IntegerField()
    product = models.ForeignKey(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default='')
