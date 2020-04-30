from django.shortcuts import render

from recipebox.models import Author, Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': recipes})


def author(request):
    recipes = Recipe.objects.all()
    authors = Author.objects.all()
    return render(request, 'author.html', {'recipes': recipes, 'authors': authors})
