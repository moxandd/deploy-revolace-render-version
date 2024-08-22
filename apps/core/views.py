from django.shortcuts import render
from apps.core.models import Post, Author
from django.views.generic import ListView, DetailView

# Create your views here.

class PostsListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'core/home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'post'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'core/author_detail.html'
    context_object_name = 'author'