from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField(max_length=40 , unique=True)
    phonenumber = models.IntegerField()
    adress= models.CharField(max_length=100)
