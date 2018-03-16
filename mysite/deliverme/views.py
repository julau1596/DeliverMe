# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from deliverme.models import Post

from forms import SignUpForm
import datetime

def index(request):
    post_list = Post.objects.all().order_by("-time")[:50]
    context = {'post_list': post_list}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['subject']
            context = {'post_list': post_list, 'title': title}
    return render(request, 'deliverme/home.html', context)

def home(request):
    return redirect('/')


def setting(request):
    return render(request, 'deliverme/setting.html', None)

def chatlog(request):
    return render(request, 'deliverme/chatlog.html', None)

def wallet(request):
    return render(request, 'deliverme/wallet.html', None)

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request, user)
            return redirect('/')
    else:   
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def new(request) :
    title = request.POST['title']
    dest = request.POST['dest']
    is_checked = "requester" in request.POST
    requester = 0
    if(is_checked): 
        requester = 1
    else:
        requester = 0
    user = request.user.username
    now = datetime.datetime.now()
    p = Post(title=title, user= user, time = now, requester = requester)
    p.save()
    # conn = sqlite3.connect('../db.sqlite3')
    # c = conn.cursor()
    # c.execute('INSERT INTO deliverme_post values(?,?,?,?)', (title,user,now,requester))
    # conn.commit()
    return redirect("/")

def map(request):
    return render(request,'deliverme/map.html');