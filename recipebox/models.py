from django.db import models
from django.utils import timezone

"""
Author Model:

    Name (CharField)
    Bio (TextField)

Recipe Model:

    Title (CharField)
    Author (ForeignKey)
    Description (TextField)
    Time Required (Charfield) (for example, "One hour")
    Instructions (TextField)
"""


class Author(models.Model):
    name = models.CharField(max_length=50)
    byline = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author}'
