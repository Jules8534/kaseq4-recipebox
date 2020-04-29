from django.shortcuts import render

from recipebox.models import Author, Recipe


def index(request):
    recipes = Recipe.objects.all()
    authors = Author.objects.all()
    return render(request, 'index.html', {'recipes': recipes, 'authors': authors})
