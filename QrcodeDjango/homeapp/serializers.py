from rest_framework import serializers
from .models import Formulaire


class FormulaireSerializer(serializers.ModelSerializer):

    class Meta:
        model=Formulaire
        fields= ('email','address','telephone','img')
    def get_photo_url(self, form):
        request = self.context.get('request')
        img = form.img.url
        return request.build_absolute_uri(img)
