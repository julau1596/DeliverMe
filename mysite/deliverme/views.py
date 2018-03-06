# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'deliverme/home.html')

def home(request):
    return redirect('/')

