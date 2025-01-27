from django.test import TestCase
from django.urls import reverse

class MyViewTests(TestCase):
    def test_my_view(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world!")
