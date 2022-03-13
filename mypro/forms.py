from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Rating

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description', 'url', "user",'photo')
        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'url':forms.TextInput(attrs={'class': 'form-control'}),
            'user':forms.TextInput(attrs={'class': 'form-control','value': ' ','id':'elder','type':'hidden'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
        }
        