from django.shortcuts import render

from .models import Article


# Create your views here.
def index(request):
    if 'search' in request.GET:
        print(request.GET)
        search = request.GET['search']
        articles = Article.objects.filter(title__icontains=search)
    else:
        articles = Article.objects.all()
    return render(request, 'djangoapp/index.html', {'articles': articles})

