# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate(self, full_name, email):
        errors = []
        if full_name == "":
            errors.append("Name cannot be empty")
        if email == "":
            errors.append("Email cannot be empty")
        elif len(User.objects.filter(email=email)) > 0:
            errors.append("Email already exists, try again.")
        return (False, errors)

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()