from datetime import datetime
from django.test import TestCase
from djangoecommerce.catalog.models import Category

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



