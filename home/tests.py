from django.test import TestCase, Client

class HomeTests(TestCase):
    def test_home_page(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "running")
