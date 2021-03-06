from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
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
    def get_absolute_url(self):
        return reverse('home')


    def delete_post(self):
        self.delete()
    @classmethod
    def search_results(cls, title):
        return cls.objects.filter(title__icontains=title).all()
    @classmethod
    def all_posts(cls):
        return cls.objects.all()
    def save_post(self):
        self.save()


class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)
    def save_rating(self):
        self.save()
    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings
    def __str__(self):
        return f'{self.post} Rating'
    
