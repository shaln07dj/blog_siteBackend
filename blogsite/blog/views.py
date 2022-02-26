
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework.views import APIView


from . import models
from blog.serializer import BlogSerialzer


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

        






