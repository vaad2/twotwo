from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Article(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    content = models.TextField(verbose_name=_('content'))

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

class Author(models.Model):
    first_name = models.CharField(verbose_name=_('first name'), max_length=255)
    last_name = models.CharField(verbose_name=_('last name'), max_length=255)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
