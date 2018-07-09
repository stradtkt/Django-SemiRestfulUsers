# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'users/index.html', context)

def create(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    errors = User.objects.validate(full_name, email)
    if len(errors) > 0:
        User.objects.create(full_name=full_name, email=email)
        return HttpResponse("Added to the database")
    else:
        for message in errors:
            messages.error(request, message)
    return redirect('/')

def new(request):
    return render(request, 'users/new.html')

def show(request, id):
    context = {"user": User.objects.get(id=id)}
    return render(request, 'users/user.html', context)

def edit(request, id):
    context = {"user": User.objects.get(id=id)}
    return render(request, 'users/edit-user.html', context)

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')

def update(request, id):
    user = User.objects.get(id=id)
    user.full_name = request.POST['full_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/')
