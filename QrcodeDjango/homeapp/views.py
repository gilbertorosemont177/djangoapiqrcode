from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import qrcode

# API REST
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Formulaire
from.serializers import FormulaireSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
from .postemail import SendEmailQrCode
from rest_framework.decorators import api_view
from rest_framework import status

class FormulaireView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'homeapp/index.html'
	

	def get(self,request):
		forms=FormulaireSerializer()
		return Response({'serializer':forms})

	
	
	def post (self, request):
		serializer=FormulaireSerializer(data=request.data)
		email=request.data['email']
		self.creationQrcode(email)
		envoyer=SendEmailQrCode(email,"test","hola marie soy el beto ","qrcodetest.png")
		envoyer.sendQrcodetoEmail()
		if not serializer.is_valid():
			return Response({'serializer': serializer})
		serializer.save()
		return HttpResponseRedirect(self.template_name)

	def creationQrcode(self,qrcodevalue):
		qrcodeimg=qrcode.make(qrcodevalue)
		qrcodeimg.save('homeapp/qrcodes/'+str(qrcodevalue)+'.png','PNG')
	
		
	

    		   
		
    
#end api rest

# Create your views here.
#this view works
# def index(request):
# 	form=PostFormulaire()
# 	if request.method == "POST":
# 	   print("post 1")
# 	   form=PostFormulaire(request.POST or None , request.FILES or None)
	   
# 	   if form.is_valid():
# 		   instance=form.save(commit=False)
# 		   instance.save()
# 		   messages.success(request,"creado")
# 		   return HttpResponse("workss!")
		   
# 	   else:
# 		   print(form.errors)
	
# 	context={"form":form}

	
# 	return render(request,'homeapp/index.html', context)

