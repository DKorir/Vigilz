from ast import Return
from this import d
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from  .models import Post ,Rating, Profile
from .forms import PostForm, RatingsForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework import viewsets
# from django.contrib.auth.models import User
from .serializers import ProfileSerializer, UserSerializer, PostSerializer
from django.http import JsonResponse




# def home(request):
#     return render(request,"home.html", {})



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddProjectView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_project.html'
    # fields = "__all__"

def rate_project(request):
    usability = request.Post.get('usabilty')
    design = request.Post.get('design')
    content = request.Post.get('content')
    rate = rate_project(usability=usability, design=design, content=content)
    rate.save()
    data = {'success': 'you have rated this project'}

    return JsonResponse(data)


def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Post.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})