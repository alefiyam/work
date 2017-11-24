from django.shortcuts import render
import json
import os
import time
from datetime import datetime
import user

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from .models import *
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

@csrf_exempt
@api_view(['POST'])
def signup(request):
    content  = {}
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    user = User.objects.create_user(username=username,
                                email=email,
                                password=password)
    content = {
        'user': unicode(user),  # `django.contrib.auth.User` instance
    }
    return Response(content)


@csrf_exempt
@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def createpost(request):
    import pdb;pdb.set_trace();
    title = request.data['title']
    text  = request.data['text']
    post  = Post.objects.create(author_id=request.user.id, title=title, text=text)
    title = post.title
    text  = post.text
    content = {
        'title' : title,
        'text' : text
    }
    return Response(content)

@csrf_exempt
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
@api_view(['PUT'])
def updatepost(request,pk):
    import pdb;pdb.set_trace();
    # user_id = request.user.id
    # title = request.data['title']
    # text  = request.data['text']
    # post  = Post.objects.create(author_id=request.user, title=title, text=text)
    # title = post.title
    # text  = post.text
    # content = {
    #     'title' : title,
    #     'text' : text
    # }
    # return Response(content)    

# from django.contrib.auth.models import User
# from rest_framework import viewsets
# from api.serializers import UserSerializer,PostSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     def get_object(self):
#         return self.request.user

# class PostViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to create post.
#     """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def create(self,request):
#         import pdb;pdb.set_trace();