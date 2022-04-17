from django.db import models


# Create your models here.
class userFiles(models.Model):
    file = models.FileField()
