from django.db import models

# Create your models here.
class Img(models.Model):
    title = models.CharField(max_length=20)
    img=models.CharField(max_length=255)
    objects=models.Manager()