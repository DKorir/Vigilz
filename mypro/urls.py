from django.urls import path, include
from .views import HomeView,ArticleDetailView, AddProjectView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns= [ 
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('api/', include(router.urls)),

    path('add_project/', AddProjectView.as_view(), name="add_project"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('search',views.search_project, name='search_project'),
   
]
