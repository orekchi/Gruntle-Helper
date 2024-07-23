
from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title
