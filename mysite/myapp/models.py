from email.policy import default
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
    #adding a new entry in the database for "expenses_monthly" meaning emi+tax+exp
    expenses_monthly = models.IntegerField(default=0)
    income_monthly = models.IntegerField(default=0)
