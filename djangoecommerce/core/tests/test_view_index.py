from django.test import TestCase


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.resp, 'index.html')





