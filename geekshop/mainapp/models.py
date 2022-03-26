from django.db import models

# Create your models here.
# class ProductCategories(models.Model):
#
#     name = models.CharField(max_length=64, unique=True)
#     descriptions = models.TextField(blank=True, null=True)
#
# def__str__(self):
# return self.name
#
# class Product(models.Model):
#
#     name = models.CharField(max_lenght = 128)
#     image = models.ImageField(upload_to='product_images',blank=True)
#     description = models.TextField(blank = True, null = True)
#     price = models.DecimalField(max_digits=8,decimal_places=2)
#     quantity = models.PositiveIntegerFelld(default = 8)
#     category = models.ForeignKey(ProductCategories, on_delete = models.)
#
#     def__str__(self):
