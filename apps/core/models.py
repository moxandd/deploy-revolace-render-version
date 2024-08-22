from django.db import models
from apps.core.data import Category

    
class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to='author_images/')
    profession = models.CharField(max_length=120, blank=True, null=False)
    bio = models.TextField(max_length=1000, blank=True, null=False)
    age = models.IntegerField(blank=True, null=False, default=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Post(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=False)
    text = models.TextField(max_length=20_000, blank=True, null=False, default='')
    image = models.ImageField(null=True, blank=True, upload_to='post_images/')
    category = models.CharField(
        max_length=30,
        choices=Category.choices,
        default=Category.DESIGN
    )
    author = models.ForeignKey(Author, null=True, blank=False, on_delete=models.SET_NULL)
    publication_date = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True, null=False)
    views = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.title