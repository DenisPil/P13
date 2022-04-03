from django.test import TestCase

from django.urls import reverse


class TestHomePage(TestCase):

    def test_main_page(self):
        path = reverse("index")
        response = self.client.get(path)
        assert response.status_code == 200 and \
            b'<h1>Welcome to Holiday Homes</h1>' \
            in response.content
