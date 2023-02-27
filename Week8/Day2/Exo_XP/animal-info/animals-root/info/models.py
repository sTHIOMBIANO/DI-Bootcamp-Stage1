from django.db import models

# Create your models here.



class Family(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Animal(models.Model):
    
    name=models.CharField(max_length=50)
    legs=models.IntegerField()
    wheight=models.CharField(max_length=50)
    height=models.CharField(max_length=50)
    speed=models.FloatField()
    familyID=models.ForeignKey(Family,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.legs} {self.wheight} {self.height} {self.speed} {self.familyID}"




    