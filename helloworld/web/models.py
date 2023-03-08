from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title