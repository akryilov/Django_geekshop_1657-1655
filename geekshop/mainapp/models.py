''' models for product and categories '''
from django.db import models


# Create your models here.
class ProductCategories(models.Model):
    ''' model for category '''

    name = models.CharField(max_length=64)
    descriptions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    ''' model for product '''

    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=8)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} | {self.category}'
