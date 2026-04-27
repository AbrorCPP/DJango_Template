from uuid import uuid4

from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=100)
    

    def __str___(self):
        return self.name 
    

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique = True)
    name = models.CharField(verbose_name="Mahsulot nomi", max_length = 150)
    price = models.DecimalField(verbose_name = "Mahsulot narxi", max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(to = Category, on_delete = models.PROTECT)
    image = models.ImageField(verbose_name = "Mahsulot rasmi", upload_to = "products/")
    description = models.TextField(verbose_name = "Mahsulot tarifi", null = True)
    in_stock = models.IntegerField(verbose_name = "Mavjud mahsulotlar",default = 1)

    def __str__(self):
        return self.name
