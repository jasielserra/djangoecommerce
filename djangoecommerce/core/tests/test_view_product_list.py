from django.test import TestCase

class ProductListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/produtos/')

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use products_list.html'''
        self.assertTemplateUsed(self.resp, 'catalog/product_list.html')