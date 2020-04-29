from django.shortcuts import render

from recipebox.models import Author, Recipe


def index(request):
    items = Recipe.objects.all()
    return render(request, 'index.html', {'data': items})
