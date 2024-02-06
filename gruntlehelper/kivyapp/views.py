from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def index(requests):
    all_articles = Article.objects.all()
    return render(requests, 'kivyapp/index.html', {'all_articles': all_articles})
