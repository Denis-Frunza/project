from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SignUp.as_view(), name='login_customer')

]
