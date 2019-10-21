# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')


def login(request):
    return render(request, 'mainapp/login.html')


def register(request):

    return render(request, 'mainapp/register.html')

def generation(request):

    return render(request, 'mainapp/generation.html')


