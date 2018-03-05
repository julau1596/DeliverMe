from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Post(models.Model):
    title = models.TextField()
    user =  models.TextField()
    message = models.TextField()
    #location =
    #destination =
    time = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    requester = models.NullBooleanField() #True if requester, false if deliverer, allowing null for testing currently

    def __str__(self):
        return self.title
