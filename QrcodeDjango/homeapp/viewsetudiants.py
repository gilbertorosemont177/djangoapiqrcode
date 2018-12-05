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
class EtudiantsInfos(APIView):

    def get(self,request,user):
        print(user)
        queryset=Formulaire.objects.filter(email=user)
        if not queryset:
                 return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
             serializer = FormulaireSerializer(queryset,many=True)
             return Response(serializer.data,status=status.HTTP_200_OK)

