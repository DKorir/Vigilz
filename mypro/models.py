from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
