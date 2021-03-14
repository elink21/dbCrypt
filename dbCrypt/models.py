from django.db import models

# Create your models here.


class CryptUser(models.Model):
    fullname = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    key = models.CharField(max_length=300)


class hashedFields(models.Model):
    fullnameHashed = models.CharField(max_length=300)
    usernameHashed = models.CharField(max_length=300)
    passwordHashed = models.CharField(max_length=300)
    emailHashed = models.CharField(max_length=300)
    addressHashed = models.CharField(max_length=300)
    phoneHashed = models.CharField(max_length=300)
    keyHashed = models.CharField(max_length=300)
