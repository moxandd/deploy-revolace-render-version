from django.urls import path
from apps.core.views import PostsListView, PostDetailView, AuthorDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('posts/<str:pk>/', PostDetailView.as_view(), name='post'),
    path('authors/<str:pk>/', AuthorDetailView.as_view(), name='author'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)