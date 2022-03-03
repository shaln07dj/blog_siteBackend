from django.urls import path
from . import views

urlpatterns=[
    path('',views.GetorCreateBlog.as_view()),
    path('/<int:id>',views.GetPutDeleteBlogView.as_view())
    
]