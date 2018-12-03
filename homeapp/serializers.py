from rest_framework import serializers
from .models import Formulaire


class FormulaireSerializer(serializers.ModelSerializer):

    class Meta:
        model=Formulaire
        fields= ('email','address','telephone','img')

    #     email = models.CharField(max_length=200,null=True)
    # address= models.CharField(max_length=200,null=True)
    # telephone= models.CharField(max_length=200,null=True)
    # img=models.FileField(null=True,blank=True)
