from django.db import models

# Create your models here.
class Formulaire(models.Model):
    email = models.CharField( max_length=250, unique=True, primary_key=True)
    address= models.CharField(max_length=200,null=True)
    telephone= models.CharField(max_length=200,null=True)
    img=models.FileField(null=True,upload_to='images/')

    def __str__(self):
        return self.email