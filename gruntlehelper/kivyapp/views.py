from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.db.models import Q


# Create your views here.

def index(request):
    if 'search' in request.GET:
        print(request.GET)
        search = request.GET['search']
        articles = Article.objects.filter(title__icontains=search)
    else:
        articles = Article.objects.all()
    return render(request, 'kivyapp/index.html', {'articles': articles})



