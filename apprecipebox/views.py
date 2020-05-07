from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from apprecipebox.models import Author, Recipe
from apprecipebox.forms import AddRecipeForm, AddAuthorForm, LoginForm


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


@login_required
def add_author(request):
    html = "generic_form.html"

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


@login_required
def add_recipe(request):
    html = "generic_form.html"

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


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})
