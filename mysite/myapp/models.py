from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    rent = models.IntegerField()
    emi = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()
