from django.test import TestCase
from django.shortcuts import resolve_url as r


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('register'))

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.resp, 'register.html')