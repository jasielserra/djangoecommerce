from django.test import TestCase
from djangoecommerce.catalog.models import Category

class CatalogModelTest(TestCase):
    def setUp(self):
        self.obj = Category(name='Eletrônico', slug='eletronicos')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())
