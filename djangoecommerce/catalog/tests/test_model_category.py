from django.test import TestCase
from djangoecommerce.catalog.models import Catalog

class CatalogModelTest(TestCase):
    def setUp(self):
        self.obj = Catalog(name='Eletrônico', slug='eletronicos')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Catalog.objects.exists())
