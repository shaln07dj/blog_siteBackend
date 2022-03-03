
from pyexpat import model
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework.views import APIView


from . import models
from blog.serializer import BlogSerialzer

import blog


class GetorCreateBlog(APIView):
    def get(self,request):
        blog_data=models.Blog.objects.all()
        blog_serialized_data=BlogSerialzer(blog_data,many=True)

        return Response(data={
            'data':blog_serialized_data.data
        })

    def post(self,request):# it takes a value from the client side or web page like form data or object data
        request_data=request.data # we are storing the request that is been send from the server to the variable
        blog_obj=BlogSerialzer(data=request_data)# we passing the data to the serializer

        if blog_obj.is_valid():
            blog_obj.save()

            return Response({
                'msg':"sucess"
            })

        return Response(status=400,data=
            blog_obj.errors
        )


class GetPutDeleteBlogView(APIView):
    def get (self,request,id):
        try:

            blog_data=models.Blog.objects.get(id=id)
            blog_serialized_data=BlogSerialzer(blog_data)

            return Response(data={'data':blog_serialized_data.data})
        except models.Blog.DoesNotExist:
            return Response(data={'data':'not present'},status=400)

    def put (self, request,id):
        try:
            request_data=request.data
            blog_data=models.Blog.objects.get(id=id)
            blog_serialized_data=BlogSerialzer(blog_data,data=request_data)
            if blog_serialized_data.is_valid():
                blog_serialized_data.save()
                return Response(data={'data':blog_serialized_data.data})
            return Response (data={'error':blog_serialized_data.errors})
        except models.Blog.DoesNotExist:
            return Response (data={'data':'not present'})

    def delete(self,request,id):
        try:
            blog_data=models.Blog.objects.get(id=id)
            blog_data.delete()
            return Response(data={'status':'deleted'})
        except models.Blog.DoesNotExist:
            return Response(data={'data':'not present'})
    

                
        


        





        






