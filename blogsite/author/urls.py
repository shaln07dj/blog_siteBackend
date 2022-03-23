from django.urls import path

from author import views

urlpatterns=[
    path('',views.GetOrCreateAuthorView.as_view()),
    path('<int:pk>/',views.GetPutDeleteAuthView.as_view())

]
