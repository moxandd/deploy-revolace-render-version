from django.db import models

class Category(models.TextChoices):
    DESIGN = "1", "Design",
    MOVIES = "2", "Movies",
    TRAVELLING = "3", "Travelling"
    

