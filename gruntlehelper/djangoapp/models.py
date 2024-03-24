from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
