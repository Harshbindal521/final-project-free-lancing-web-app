import Lctl
from os import name
from django.db import models
from django.db.models.base import Model
from django.core.files.storage import FileSystemStorage, default_storage
fs = FileSystemStorage(location='/media/Lctl/images')


# Create your models here.

class freelancer(models.Model):
    name= models.CharField(max_length=25)
    username= models.CharField(max_length=25)
    skills= models.CharField(max_length=25)
    desc= models.CharField(max_length=250 , default=" ")
    aboutdesc = models.CharField(max_length=2000, default="")
    payperhr= models.CharField(max_length=3 , default="250")
    country = models.CharField(max_length=30, default="")
    phn= models.CharField(max_length=15, default="9999999999")
    freelancer_photo = models.ImageField(upload_to="Lctl/images", default="")


    def __str__(self):
        return self.username
    
    

class order(models.Model):
    client_username = models.CharField(max_length=25)
    client_email = models.EmailField( max_length=254)
    freelancer_username = models.CharField(max_length=25)
    work_desc= models.CharField(max_length=500)
    order_amount = models.CharField(max_length=10)
    order_status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id}"

class img(models.Model):
    photo = models.ImageField(storage=fs)