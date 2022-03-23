from dataclasses import field, fields
import imp
from pyexpat import model
from rest_framework import serializers
from author import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # username=serializers.SerializerMethodField(read_only=True)
    id=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User
        fields='__all__'

    def get_id(self,obj):
        return obj.id

    # def get_name(self,obj):
    #     return obj.username



class AuthorSerializer(serializers.ModelSerializer):
    user_details=UserSerializer(source='user',read_only=True,many=False)
    class Meta:
        model=models.Authors
        fields='__all__'
        # fields=['bio','avatar']
        extra_kwargs={
            'user_details':{'write_only':True},

        }