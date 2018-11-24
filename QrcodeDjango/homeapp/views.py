from django.shortcuts import render
from homeapp.forms import PostFormulaire
from homeapp.models import Formulaire
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
	form=PostFormulaire
	if request.method == "POST":
	   print("post 1")
	   form=PostFormulaire(request.POST)
	   print(form)
	   if form.is_valid():
		   print("post 2")
		#    email= request.POST.get('email','')
		#    print(email)
		#    address=request.POST.get('address','')	
		#    print(address)
		#    telephone=request.POST.get('telephone','')
		#    img=request.POST.get('img','')
		#    formulaireobjetModel= Formulaire(email=email,address=address,telephone=telephone,img=img)
		#    formulaireobjetModel.save()
		   print(form.cleaned_data)
	   else:
		   print(form.errors)
	
	context={"form":form}

	
	return render(request,'homeapp/index.html', context)
