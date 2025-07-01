from django.test import TestCase, Client
from .models import Publisher

class TestPublisherModel(TestCase):
    """Testowanie modelu Publisher."""
    def setUp(self):
        self.p = Publisher(name='Packt', website='www.packt.com', email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)
    
    def test_str_representation(self):
        self.assertEqual(str(self.p), "Packt")

class TestGreetingView(TestCase):
    """Testowanie widoku powitalnego."""
    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/test/greeting')
        self.assertEqual(response.status_code, 200)
