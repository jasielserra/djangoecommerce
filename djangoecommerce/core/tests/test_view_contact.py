from django.test import TestCase

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
               ('<input',2),
                ('type="text"',2),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


