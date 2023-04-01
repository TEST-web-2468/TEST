from django.shortcuts import render
from django.http import HttpResponse as h
from .models import *
# Create your views here.

def test(requests , val , va):
    create_user = user.objects.create(name = val , msg=va)

    gr = group.objects.create(name = val , msg=va)

    gr.save()
    create_user.save()

    return h('done')