from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(max_length=4000)
    code_example = RichTextField(max_length=4000)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
