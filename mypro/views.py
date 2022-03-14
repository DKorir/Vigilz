from ast import arg
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from  .models import Post ,Rating
from .forms import PostForm, RatingsForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# def home(request):
#     return render(request,"home.html", {})

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

def Rate(request, post_id):
    post = Post.objects.get(post_id=post.id)
    user = request.user
    if request.method == "POST":
        form = RatingsForm(request.POST)
        rate = form.save(commit=False)
        rate.user = user
        rate.post = post
        rate.save()
        return HttpResponseRedirect(reverse('article-detail', args=[post_id]))
    else:
        form = RatingsForm()
    template_name = 'article_detail.html'
    context = {
        'form': form,
        'post': post
    }
    # return HttpResponse(template.render(context,request))