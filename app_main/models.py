from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=100)
    

    def __str___(self):
        return self.name