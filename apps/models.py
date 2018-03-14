from django.db import models
from signup import settings
# Create your models here.
class Sign(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,primary_key=True)
    contact=models.CharField(max_length=50)
    profile_picture=models.ImageField(null=True,blank=True,upload_to='img/')

    def __str__(self):
        return self.fname