from django.db import models

# Create your models here.

# fields of product table
class Product(models.Model):
    name=models.CharField(max_length=300,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="")
    details=models.CharField(max_length=5000,default="")


    def __str__(self):
        return self.name
