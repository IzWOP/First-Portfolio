from django.urls import include, path
from . import views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all(). order_by("-date")[:5],
                              template_name="blog/blog.html")),
     path('<int:pk>', DetailView.as_view(model=Post, template_name='blog/post.html')),
]
