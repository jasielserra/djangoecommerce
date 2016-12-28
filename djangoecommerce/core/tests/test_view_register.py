from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.contrib.auth import get_user_model

User = get_user_model()



class RegisterTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('register'))

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.resp, 'register.html')

class RegisterPostValid(TestCase):
    def setUp(self):
        data = dict(username='jasi', password1='teste123', password2='teste123')
        self.resp = self.client.post(r('register'), data)

    def test_post(self):
        """ Valid POST should redirect to /index/ """
        self.assertRedirects(self.resp, r('index'))

    def test_quantity(self):
        self.assertEquals(User.objects.count(), 1)