# from operator import mod
from django.db import models

# Create your models here.
class UploadDB(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to='media')
    ulrfile= models.CharField(max_length=100)


