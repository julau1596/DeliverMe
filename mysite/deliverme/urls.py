from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from django.views.generic import ListView, DetailView
from deliverme.models import Post

urlpatterns = [
    #Fetches Post objects, latest 50 posts sorted by date/time, puts them into main.html
    #url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-time")[:50], template_name="deliverme/main.html")),
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^login/home/$', views.home),
    url(r'^signup/$', views.signup, name='signup'),

]
