from django.test import TestCase
from djangoecommerce.catalog.models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='informatica', slug='info')

    def test_create(self):
        product = Product.objects.create(name='MacBook Air', slug='mac-book', category=self.category,
                            description='Lorem ipsulum', price=7.560)

        self.assertTrue(Product.objects.exists())

