from django.test import TestCase
from djangoecommerce.catalog.models import Product
from model_mommy import mommy

class ProductListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/catalogo/')
        self.products = mommy.make('catalog.Product', _quantity=5)
       #self.category = Category.objects.create(name='informatica', slug='info')
       #self.products = Product.objects.create(name='MacBook Air', slug='mac-book', category=self.category,
       #                                       description='Lorem ipsulum', price=7.560)

    def tearDown(self):
        Product.objects.all().delete()

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use products_list.html'''
        self.assertTemplateUsed(self.resp, 'catalog/product_list.html')

    def test_product_in_context(self):
        self.assertTrue('products' in self.resp.context)

    def test_quantity_of_product(self):
        product_list = self.resp.context['products']
        self.assertEquals(product_list.count(), 5)

