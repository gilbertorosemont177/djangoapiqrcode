from django.db import models

# Create your models here.
class Formulaire(models.Model):
    email = models.CharField(max_length=200,default='')
    address= models.CharField(max_length=200,default='')
    telephone= models.CharField(max_length=20,default='')
    img=models.ImageField()

    def __str__(self):
        return self.email

