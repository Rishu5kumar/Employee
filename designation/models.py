from django.db import models

# Create your models here.

class designation(models.Model):
    des_name=models.CharField(max_length=255)