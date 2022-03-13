from django.urls import path
from .views import HomeView,ArticleDetailView, AddProjectView
urlpatterns= [ 
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_project/', AddProjectView.as_view(), name="add_project"),
]
