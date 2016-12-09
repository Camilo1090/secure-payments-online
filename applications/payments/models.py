from __future__ import unicode_literals

from django.db import models

from applications.clients.models import *

# Create your models here.


class Payment(models.Model):
    order_id = models.IntegerField(unique=True)
    amount = models.FloatField()
    is_paid = models.BooleanField()
    
    card = models.ForeignKey(Card)
    email = models.EmailField()
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
