from django.shortcuts import render

from recipebox.models import Author, Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe(request, num=1):
    recipe = Recipe.objects.get(id=num)
    return render(request, 'recipe.html', {'recipe': recipe})


def author(request, num=1):
    # recipes = Recipe.objects.all()
    author = Author.objects.get(id=num)
    return render(request, 'author.html', {'author': author})
