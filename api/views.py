from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication
from clases import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from api import serializers, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnUser,)
    filter_backends= (filters.SearchFilter,)
    search_fields= ('cnickname', 'cfirstname')

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.CountrySerializer
    queryset = models.Country.objects.all()

class CityViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.CitySerializer
    queryset = models.City.objects.all()

class GameViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.GameSerializer
    queryset = models.Game.objects.all()