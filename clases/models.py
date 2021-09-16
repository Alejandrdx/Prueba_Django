from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from typing import Tuple

from django.db.models.fields import NullBooleanField

class Country(models.Model):
    cnameCountry = models.CharField(max_length=45)


class City(models.Model):
    nidCountry = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    cnameCity = models.CharField(max_length=255)


class Gender(models.Model):
    cname = models.CharField(max_length=45)
    cabbreviation = models.CharField(max_length=45)

class UserManager(BaseUserManager):
    
    def create_user(self, cnickname, cfirstname, clastname, dbirthdate, cmail, cavatar, cphone, clongitude, clatitude, cdescription, cipUser, nidGender, nidCity, password=None):
        
        if not cmail:
            raise ValueError('Usuario debe tener un email')

        cmail = self.normalize_email(cmail)

        
        user = self.model(cnickname=cnickname, password=password, cfirstname=cfirstname, clastname=clastname, dbirthdate=dbirthdate, cmail=cmail, cavatar=cavatar, cphone=cphone, clongitude=clongitude, clatitude=clatitude, cdescription=cdescription, cipUser=cipUser, nidGender=nidGender, nidCity=nidCity)

        user.set_password(password)
        user.save(using=self._db)


        return user

    def create_superuser(self, cnickname, password, cfirstname, clastname, dbirthdate, cmail, cavatar, cphone, clongitude, clatitude, cdescription, cipUser, nidGender, nidCity):
        user = self.create_user(self, cnickname, password, cfirstname, clastname, dbirthdate, cmail, cavatar, cphone, clongitude, clatitude, cdescription, cipUser, nidGender, nidCity)

        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    cnickname = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    cfirstname = models.CharField(max_length=45)
    clastname = models.CharField(max_length=45)
    dbirthdate = models.DateField()
    cmail = models.CharField(max_length=255)
    cavatar = models.CharField(max_length=100, null=True, blank=True, default=None)
    cphone = models.CharField(max_length=11, null=True, blank=True, default=None)
    clongitude = models.CharField(max_length=45, null=True, blank=True, default=None)
    clatitude = models.CharField(max_length=45, null=True, blank=True, default=None)
    cdescription = models.TextField(null=True, blank=True, default=None)
    cipUser = models.CharField(max_length=45, null=True, blank=True, default=None)
    nidGender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    nidCity = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'cnickname'
    REQUIRED_FIELDS = ['cfirstname']

    def get_full_name(self):
        '''Obtener nombre completo del usuario'''
        return self.cfirstname

    def get_short_name(self):
        '''Obtener nombre corot del usuario'''
        return self.cfirstname

    def __str__(self):
        '''Retornar cadena representando nuestro usuario'''
        return self.cfirstname


class Match(models.Model):
    nidUser1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user1')
    nidUser2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user2')
    buser1Like = models.BooleanField(default=False)
    buser2Like = models.BooleanField(default=False)
    bmatch = models.BooleanField(default=False)

class Room(models.Model):
    cidMatch = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True)

class Message(models.Model):
    tmessage = models.TextField()
    ddate = models.DateTimeField()
    nidRoom = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    nidUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class characteristic_user(models.Model):
    cname = models.CharField(max_length=45)

class detail_user(models.Model):
    nidUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nidCharacteristic = models.ForeignKey(characteristic_user, on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    cname = models.CharField(max_length=45)
    cicon = models.CharField(max_length=100)
    tdescription = models.TextField()

class Game(models.Model):
    cname = models.CharField(max_length=45)
    drelaseDate = models.DateField()
    cimage = models.CharField(max_length=100)
    nidCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class detail_category(models.Model):
    nidUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nidCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class detail_game(models.Model):
    nidUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nidGame = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)


