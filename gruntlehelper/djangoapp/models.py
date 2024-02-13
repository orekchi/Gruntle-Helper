from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field(max_length=4000, config_name='extends')
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
