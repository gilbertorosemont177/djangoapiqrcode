# not apirest
# from django.shortcuts import render
# from homeapp.forms import PostFormulaire
# from homeapp.models import Formulaire
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# from django.urls import reverse
# from django.contrib import messages
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

class FormulaireListView(APIView):
    	
	def get(self,request):                       
		snippets = Formulaire.objects.all()
		print("helllo get all")
		print(snippets)                           
		serializer = FormulaireSerializer(snippets,many=True)                                     
		return Response(serializer.data)
	