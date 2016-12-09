from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import urllib
import urllib2
import json

from forms import *
from models import *
from applications.clients.models import *

# Create your views here.


def pay(request):
    form = PayForm()
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            order_id = request.GET['order_id']
            amount = request.GET['amount']
            card_number = form.cleaned_data['card_number']
            card_month = form.cleaned_data['card_month']
            card_year = form.cleaned_data['card_year']
            card_cvv = form.cleaned_data['card_cvv']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            card = None
            try:
                card = Card.objects.get(number=card_number, month=card_month, year=card_year, cvv=card_cvv)
            except Exception as ex:
                # front-end payment rejected
                print ex.message
                return HttpResponse('Payment Error')
            if card:
                if card.balance >= amount:
                    payment = Payment(order_id=order_id, amount=amount, is_paid=False, card=card, email=email, country=country, state=state, city=city, address=address)
                    payment.save()
                    new_balance = card.balance - amount
                    card.balance = new_balance
                    card.save()
                    payment.is_paid = True
                    payment.save()
                    if answer_online(payment):
                        return HttpResponse('Payment Succesful')
                    else:
                        return HttpResponse('Payment Error')
                else:
                    # front-end payment rejected
                    print 'not enough money'
                    return HttpResponse('Payment Error')
        else:
            return HttpResponse('Payment Error')
                    
    
    return render(request, 'payments/pay.html', {'form': form})
    
    
def answer_online(payment):
    url = 'https://admisionesabc-andresf01.c9users.io/pagos/online'
    values = {
        # 'format': 'json',
        'order_id': payment.order_id,
    }
    
    data = urllib.urlencode(values)
    full_url = url + '?' + data
    response = urllib2.urlopen(full_url)
    the_page = response.read()
    
    if the_page == 'OK':
        return True
    else:
        return False
