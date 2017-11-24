from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')      

# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     def create(self, validated_data):
#         import pdb;pdb.set_trace();
#         # user = UserModel.objects.create(
#         #     username=validated_data['username']
#         # )
#         # user.set_password(validated_data['password'])
#         # user.save()
#         # self._kwargs['context']['request'].user.id

#         return post

#     class Meta:
#         model = Post
#         fields = ('title', 'text')