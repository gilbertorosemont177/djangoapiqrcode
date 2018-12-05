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
from django.shortcuts import redirect

def index(request):
  return HttpResponseRedirect('/form')
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
		envoyer=SendEmailQrCode(email,"test","hello test qrcode ","qrcodetest.png")
		envoyer.sendQrcodetoEmail()
		if not serializer.is_valid():
			return Response({'serializer': serializer})
		serializer.save()
		return HttpResponseRedirect('/form')

	def creationQrcode(self,qrcodevalue):
		qrcodeimg=qrcode.make(qrcodevalue)
		qrcodeimg.save('homeapp/qrcodes/qrcodetest.png','PNG')
	
		
