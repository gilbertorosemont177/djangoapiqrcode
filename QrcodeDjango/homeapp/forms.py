from django import forms
from .models import Formulaire

# class FormulaireForm(forms.Form):
#     email = forms.CharField()
#     address= forms.CharField()
#     telephone= forms.CharField()
#     #img = forms.ImageField()
class PostFormulaire(forms.ModelForm):
    class Meta:
        model=Formulaire
        fields=[

            "email",
            "address",
            "telephone",
            "img",
        ]


   

   
