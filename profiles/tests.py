from django.test import TestCase
from django.test import Client

from django.urls import reverse


class TestProfiles(TestCase):

    def test_profiles_page(self):
        path = reverse("profiles_index")
        response = self.client.get(path)
        print(path, response, '_________________________')
        assert response.status_code == 200 and \
            b'<h1>Welcome to Holiday Homes</h1>' \
            in response.content
