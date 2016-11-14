from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def login(self, email, password):
        pass

    def register(self, request, first_name, last_name, email, password, confirm):
        canGoOn = True
        if (len(first_name) < 2):
            canGoOn = False
            messages.error(request, 'First name too short')
        if (not first_name.isalpha()):
            canGoOn = False
            messages.error(request, "First name must be only letters")
        if (len(last_name) < 2):
            canGoOn = False
            messages.error(request, "Last name too short")
        if (not last_name.isalpha()):
            canGoOn = False
            messages.error(request, "Last name must be only letters")
        if (not EMAIL_REGEX.match(email)):
            canGoOn = False
            messages.error(request, "Not a valid email")
        if (not password == confirm):
            canGoOn = False
            messages.error(request, "Passwords don't match")
        if (len(password) < 8):
            canGoOn = False
            messages.error(request, "Password too short")
        return canGoOn

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField()
    password_hash = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
