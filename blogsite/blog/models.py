
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.title)

class Comments(models.Model):
    pass

