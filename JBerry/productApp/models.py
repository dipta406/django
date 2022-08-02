from distutils.command.upload import upload
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField(max_length=30)
    desc = models.TextField(max_length=2000)
    price = models.FloatField()
    weight = models.FloatField()
    category = models.TextField(max_length=10)
    delivery = models.SmallIntegerField(default=7)
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='upload')
 

    def __str__(self) -> str:
        return f'Product({self.pid} | {self.title})'
