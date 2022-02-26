
from rest_framework import serializers
from blog import models
from . import models


class BlogSerialzer(serializers.ModelSerializer):
    class Meta:
        model=models.Blog
        fields='__all__' 
    




