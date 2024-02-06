
from django.urls import path, include
from . import views

app_name = 'kivyapp'


urlpatterns = [
    path('', views.index, name='index'),
]
