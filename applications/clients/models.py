# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Card(models.Model):
    MONTH_CHOICES = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    
    YEAR_CHOICES = (
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
    )
    
    
    number = models.IntegerField(unique=True, verbose_name='Número de Tarjeta')
    month = models.CharField(max_length=2, choices=MONTH_CHOICES, verbose_name='Mes')
    year = models.CharField(max_length=2, choices=YEAR_CHOICES, verbose_name='Año')
    cvv = models.IntegerField(verbose_name='CVV')
    balance = models.FloatField()
    client = models.ForeignKey(Client)
    
