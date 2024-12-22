from django.db import models

# Create your models here.

class Table(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    image = models.ImageField(upload_to="portal/images", default="")


class TableBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=15,default="")  # Assuming phone number is a string
    image = models.ImageField(upload_to="portal/images", default="")

    def __str__(self):
     return self.name


