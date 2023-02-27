from django.db import models

# Create your models here.
class MainPage(models.Model):
    title = models.CharField(default="", max_length=200)
    description = models.TextField(default="", max_length=2000)

    place = models.CharField(default="", max_length=200)
    