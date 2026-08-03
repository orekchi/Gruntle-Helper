
from django.urls import path, include
from . import views

app_name = "bitcoinapp"
urlpatterns = [
    path('', views.index, name='index'),
]
