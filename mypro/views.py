from pyexpat import model
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from  .models import Post 
# def home(request):
#     return render(request,"home.html", {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    
