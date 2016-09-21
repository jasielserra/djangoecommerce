from django.test import TestCase
from django.core import mail

class ContactTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contato/')

    def test_get(self):
        '''GET /Contact/ must return status code 200.'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''Must use contact.html'''
        self.assertTemplateUsed(self.resp, 'contact.html')

    def test_html(self):
        '''HTML must contains input tags.'''
        tags = (('<form',1),
               ('<input',3),
                ('type="text"',1),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_form_error(self):
        data = {'name':'', 'message':'','email':''}
        response = self.client.post('/contato/', data)

        self.assertFormError(response,'form','name','Este campo é obrigatório.')
        self.assertFormError(response,'form','email','Este campo é obrigatório.')
        self.assertFormError(response,'form','message','Este campo é obrigatório.')

    def test_form_ok(self):
        data = {'name':'Jasi', 'message':'Minha Mensagem','email':'jasiel_serra@hotmail.com'}
        response = self.client.post('/contato/', data)
        self.assertTrue(response.context['success'])
        self.assertEqual(len(mail.outbox),1)
        self.assertEquals(mail.outbox[0].subject,'Contato do Django E-Commerce')




