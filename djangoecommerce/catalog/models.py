from django.db import models


class Catalog(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
