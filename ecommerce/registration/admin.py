from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


admin.site.register(CustomUser)

