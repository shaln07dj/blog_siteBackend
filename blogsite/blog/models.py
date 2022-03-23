
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image_url=models.URLField(null=True)
    cover_image=models.ImageField(null=True,blank=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return (self.title)



