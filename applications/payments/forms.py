# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
import urllib
import urllib2

from models import *
from applications.clients.models import *


class PayForm(ModelForm):
    
    MONTH_CHOICES = (
        ('01', '01 - Enero'),
        ('02', '02 - Febrero'),
        ('03', '03 - Marzo'),
        ('04', '04 - Abril'),
        ('05', '05 - Mayo'),
        ('06', '06 - Junio'),
        ('07', '07 - Julio'),
        ('08', '08 - Agosto'),
        ('09', '09 - Septiembre'),
        ('10', '10 - Octubre'),
        ('11', '11 - Noviembre'),
        ('12', '12 - Diciembre'),
    )
    
    YEAR_CHOICES = (
        ('16', '2016'),
        ('17', '2017'),
        ('18', '2018'),
        ('19', '2019'),
        ('20', '2020'),
        ('21', '2021'),
        ('22', '2022'),
        ('23', '2023'),
        ('24', '2024'),
        ('25', '2025'),
        ('26', '2026'),
        ('27', '2027'),
    )
    
    owner_first_name = forms.CharField()
    owner_last_name = forms.CharField()
    card_number = forms.IntegerField()
    card_month = forms.ChoiceField(choices=MONTH_CHOICES)
    card_year = forms.ChoiceField(choices=YEAR_CHOICES)
    card_cvv = forms.IntegerField()
    
    
    def __init__(self, *args, **kwargs):
        super(PayForm, self).__init__(*args, **kwargs)
        
    
    class Meta:
        model = Payment
        fields = ('email', 'country', 'state', 'city', 'address',)
        exclude = ('order_id', 'amount', 'is_paid',)
        
        
    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if not card_number.isdigit():
            raise forms.ValidationError("El numero de tarjeta debe contener solo numeros.")
        try:
            card = Card.objects.get(number=card_number)
        except Exception:
            raise forms.ValidationError("El numero de tarjeta no se encuentra registrado.")
        return card_number
        
        
    def clean_card_cvv(self):
        card_cvv = self.cleaned_data['card_cvv']
        if not card_number.isdigit():
            raise forms.ValidationError("El CVV debe contener solo numeros.")
        return card_cvv