from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")

    image = models.ImageField(upload_to="static", default="", null=True)

    seats = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    space = models.CharField(max_length=200, default="")

    price = models.IntegerField(default=0)
    description = models.TextField(max_length=2000, default="")

    def __str__(self):
        return f"{self.brand} {self.name}"
    

