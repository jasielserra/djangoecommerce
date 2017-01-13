from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from model_mommy import mommy
from django.conf import settings

from djangoecommerce.accounts.models import User


class UpdatePasswordTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {
            'old_password': '123', 'new_password1': 'teste123', 'new_password2': 'teste123'
        }
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('teste123'))
