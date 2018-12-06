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

    def validate(self, data):
        if not data['address']:
           raise serializers.ValidationError({'address': ['this field is not valid']})
        if not data['telephone']:
           raise serializers.ValidationError({'telephone': ['this field is not valid']})
        if not data['img']:
            raise serializers.ValidationError({'img': ['this field is not valid']})
        return data



