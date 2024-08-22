from django.contrib import admin
from apps.core.models import Post, Author

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)