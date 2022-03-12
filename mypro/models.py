from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    def delete_post(self):
        self.delete()
    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()
    @classmethod
    def all_posts(cls):
        return cls.objects.all()
    def save_post(self):
        self.save()

