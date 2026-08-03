from django.shortcuts import render
from .models import ResourceModel
from django.http import HttpResponse


# Create your views here.
def index(request):
    resource = ResourceModel.objects.all().order_by('name')
    print(resource)
    return render(request, 'mainpageapp/index.html', {'resource': resource})
