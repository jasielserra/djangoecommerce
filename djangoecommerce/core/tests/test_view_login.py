from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy


class LoginTestView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('login'))
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use login.html'''
        self.assertTemplateUsed(self.resp, 'login.html')

class ValidloginTest(TestCase):
    def setUp(self):
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
        data = dict(username=self.user.username, password=123)
        self.resp = self.client.post(r('login'), data)

    def tearDown(self):
        self.user.delete()

    def test_validlogin(self):
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(self.resp, redirect_url)

    def test_user_authenticated(self):
        self.assertTrue(self.resp.wsgi_request.user.is_authenticated())

class InValidloginTest(TestCase):
    def setUp(self):
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
        data = dict(username=self.user.username, password=1234)
        self.resp = self.client.post(r('login'), data)


    def tearDown(self):
        self.user.delete()

    def test_get(self):
        '''GET / must return status code 200.'''
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        '''Must use login.html'''
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_invalidlogin(self):

        error_msg = ('Por favor, entre com um Apelido / Usuário e senha corretos.'
                     ' Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(self.resp, 'form', None, error_msg)
