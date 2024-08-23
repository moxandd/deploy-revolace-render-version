from django.shortcuts import render
from apps.core.models import Post, Author
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class PostsListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'core/home.html'
    context_object_name = 'posts'
    paginate_by = 6


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Post.objects.filter(title__icontains=query).order_by('-publication_date')
        return Post.objects.all()




class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
          post_id = self.kwargs.get('pk')
          print(post_id)
          post = get_object_or_404(Post, id=post_id)

          # Update the view count on each visit to this post.
          if post:
               post.views = post.views + 1
               post.save()

          return post


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'core/author_detail.html'
    context_object_name = 'author'