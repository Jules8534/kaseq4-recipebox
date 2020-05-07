from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    timeRequired = models.CharField(max_length=30)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.author}'
