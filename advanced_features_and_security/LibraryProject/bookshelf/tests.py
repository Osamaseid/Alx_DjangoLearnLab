
from django.test import TestCase

class SecurityTests(TestCase):
    def test_csp_headers(self):
        response = self.client.get('/')
        self.assertIn('Content-Security-Policy', response.headers)

    def test_csrf_protection(self):
        response = self.client.get('/your-form-url/')
        self.assertContains(response, 'csrfmiddlewaretoken')
