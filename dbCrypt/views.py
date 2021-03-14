from django.shortcuts import render
from dbCrypt.models import CryptUser, hashedFields
from django.http import JsonResponse
import json
from cryptography.fernet import Fernet
import hashlib

# Create your views here.

ownKey = 'nt45Pma7FexZ_L6fZU9wrNdVaE9eyvz4xbQ1ktdXxFk='


def hashMsg(msg: str) -> str:
    m = hashlib.shake_256()

    m.update(msg.encode('utf-8'))

    key = '0'+str(m.hexdigest(11))

    return key


def index(request):
    return render(request, 'signup.html', context={})


def encryptData(text: str) -> bytes:
    fernet = Fernet(ownKey)
    return str(fernet.encrypt(text.encode()))[2:-1]


def decryptData(text: str) -> str:
    fernet = Fernet(ownKey)
    text = text.encode()
    return fernet.decrypt(text).decode()


def saveUser(request):
    # Checking if username already exists
    users = CryptUser.objects.all()
    res = {'status': 200}

    for user in users:
        print(user.username+"|||||"+decryptData(user.username))
        if decryptData(user.username) == request.GET['username']:
            return JsonResponse({'status': '400'})

    newUser = CryptUser()
    newUser.username = encryptData(request.GET['username'])
    newUser.fullname = encryptData(request.GET['fullname'])
    newUser.email = encryptData(request.GET['email'])
    newUser.password = encryptData(request.GET['password'])
    newUser.phone = encryptData(request.GET['phone'])
    newUser.address = encryptData(request.GET['address'])
    newUser.key= hashMsg(newUser.username)

    userHashed= hashedFields()

    userHashed.usernameHashed= hashMsg(newUser.username)
    userHashed.fullnameHashed= hashMsg(newUser.fullname)
    userHashed.emailHashed= hashMsg(newUser.email)
    userHashed.phoneHashed= hashMsg(newUser.phone)
    userHashed.addressHashed= hashMsg(newUser.address)
    userHashed.passwordHashed= hashMsg(newUser.password)
    userHashed.keyHashed= newUser.key

    userHashed.save()
    newUser.save()

    return JsonResponse(res)
