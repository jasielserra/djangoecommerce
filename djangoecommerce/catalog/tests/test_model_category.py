from datetime import datetime
from django.test import TestCase
from djangoecommerce.catalog.models import Category
from django.shortcuts import resolve_url as r

class CategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category(name='Eletrônico', slug='eletronicos')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_has_created_at(self):
        '''Category must have an auto created_at.'''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual(str(self.obj), 'Eletrônico')

    def test_get_absolute_url(self):
        url = r('catalog:category', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())



