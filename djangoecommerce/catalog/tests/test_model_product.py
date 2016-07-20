from datetime import datetime
from django.test import TestCase
from djangoecommerce.catalog.models import Product, Category
from django.shortcuts import resolve_url as r

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='informatica', slug='info')
        self.product = Product.objects.create(name='MacBook Air', slug='mac-book', category=self.category,
                                              description='Lorem ipsulum', price=7.560)

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_product_has_created_at(self):
        '''Product must have an auto created_at'''
        self.assertIsInstance(self.product.created_at, datetime)

    def test_str(self):
        self.assertEqual(str(self.product), 'MacBook Air')

    def test_get_absolute_url(self):
        url = r('catalog:product', slug=self.product.slug)
        self.assertEqual(url, self.product.get_absolute_url())

