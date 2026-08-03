
from django.urls import path, include
from . import views

app_name = "pythonapp"
urlpatterns = [
    path('', views.index, name='index'),
]
