from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    full_name = models.CharField(max_length=200, default="")

    email = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.full_name}"

    