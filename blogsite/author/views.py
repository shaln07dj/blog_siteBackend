from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from author import models, serializer


# Create your views here.

class GetOrCreateAuthorView(ListCreateAPIView):
    serializer_class=serializer.AuthorSerializer
    queryset=models.Authors.objects.all()

class GetPutDeleteAuthView(RetrieveUpdateDestroyAPIView):
    serializer_class=serializer.AuthorSerializer
    queryset=models.Authors.objects.all()





