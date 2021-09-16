from re import S
from django.contrib.auth.password_validation import password_changed
from django.db.models import fields
from rest_framework import serializers
from rest_framework.mixins import RetrieveModelMixin
from clases import models


class UserSerializer(serializers.ModelSerializer):
    """serializa Usuario"""

    class Meta:
        model= models.User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }



    def create(self, validated_data):
        """crear y retornar nuevo usuario"""
        user = models.User.objects.create_user(
            cnickname = validated_data['cnickname'],
            password = validated_data['password'],
            cfirstname = validated_data['cfirstname'],
            clastname = validated_data['clastname'],
            dbirthdate = validated_data['dbirthdate'],
            cmail = validated_data['cmail'],
            cavatar = validated_data['cavatar'],
            cphone = validated_data['cphone'],
            clongitude = validated_data['clongitude'],
            clatitude = validated_data['clatitude'],
            cdescription = validated_data['cdescription'],
            cipUser = validated_data['cipUser'],
            nidGender = validated_data['nidGender'],
            nidCity = validated_data['nidCity'],
        )

        #user = models.User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= models.Country
        fields='__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model= models.City
        fields='__all__'

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Game
        fields='__all__'

