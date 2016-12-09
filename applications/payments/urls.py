from django.conf.urls import url

import views

urlpatterns = [
    url(r'^pay', views.pay, name='pay'),
]
