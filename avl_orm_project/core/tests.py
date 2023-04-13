from django.test import TestCase
class FeriadosTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/feriados')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'Hoje')
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'feriados.html')