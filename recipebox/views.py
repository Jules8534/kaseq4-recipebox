from django.shortcuts import render

from recipebox.models import Author, NewsItem


def index(request):
    items = NewsItem.objects.all()
    return render(request, 'index.html', {'data': items})
