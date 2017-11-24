from django.shortcuts import render
import json
import os
import user
import requests

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


def signup(request):
    response = requests.post("http://localhost:8000/api/signup")
    # content = response.json()
    # request.session["user_token"] = content["token"]
    from django.http import JsonResponse
    return JsonResponse({'error': 'Some Error'}, status=200)
    # return Response(x)

def signin(request):
    # response = requests.post("api/signin/",headers={'Authorization':'Bearer{}',format("12345")})
    return Response(response.json())

def createpost(request):
    # import pdb;pdb.set_trace();
    token = request.session["user_token"]
    print(token)
    payload = {}
    payload['token'] = token
    # response = requests.post("api/create_post/",params=payload)
    # response = requests.post("api/create_post/",headers={'Authorization':'Bearer{}',format(token)})
    # return Response(response.json())        

# {
#     "username": "raj",
#     "email": "raj@gmail.com",
#     "password":"12345678"
# }