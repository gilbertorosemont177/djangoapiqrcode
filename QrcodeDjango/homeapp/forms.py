from django import forms

class FormulaireForm(forms.Form):
   
    email = forms.CharField(max_length=200,default='')
    address= forms.CharField(max_length=200,default='')
    telephone= forms.CharField(max_length=20,default='')
    img=forms.ImageField()

    def __str__(self):
        return self.email

