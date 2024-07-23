
from django.urls import path, include
from . import views

app_name = "linuxapp"
urlpatterns = [
    path('', views.index, name='index'),
]
