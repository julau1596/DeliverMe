# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from deliverme.models import Post
from deliverme.models import User

admin.site.register(Post)
admin.site.register(User)
