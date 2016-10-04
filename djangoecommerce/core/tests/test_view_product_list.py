from django.test import TestCase
from djangoecommerce.catalog.models import Product

class ProductListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/catalogo/')
        self.products = self.resp.context['products']

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use products_list.html'''
        self.assertTemplateUsed(self.resp, 'catalog/product_list.html')

    def has_product(self):
        self.assertIsInstance(self.products, Product)

#    def test_quantity_of_product(self):
#        self.assertEquals(self.products.count(), 4)

