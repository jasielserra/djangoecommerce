from django.test import TestCase
from django.shortcuts import resolve_url as r
from djangoecommerce.catalog.models import Product
from djangoecommerce.catalog.models import Category

class ProductTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Informatica', slug='info')
        self.product = Product.objects.create(name='MacBook Air',
                                         slug='macbook',
                                         category=self.category,
                                         description='',
                                         price=5.000,
                                         )

        self.resp = self.client.get(r('catalog:product', slug=self.product.slug))

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use product.html'''
        self.assertTemplateUsed(self.resp, 'catalog/product.html')