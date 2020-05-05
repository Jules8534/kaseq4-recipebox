from django.shortcuts import render, reverse, HttpResponseRedirect

from apprecipebox.models import Author, Recipe
from apprecipebox.forms import AddRecipeForm, AddAuthorForm


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html',
                  {'author': author, 'recipes': recipes})


def add_author(request):
    html = "author_add.html"

    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})


def add_recipe(request):
    html = "recipe_add.html"

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                timeRequired=data['timeRequired'],
                instructions=data['instructions'],

            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm()

    return render(request, html, {"form": form})
