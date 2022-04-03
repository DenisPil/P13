from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from .models import Address, Letting

class TestProfiles(TestCase):

    def test_Lettings_page(self):
        path = reverse("lettings_index")
        response = self.client.get(path)
        assert response.status_code == 200 and \
            b'<h1>Lettings</h1>' \
            in response.content

    def test_letting_detail(self):
        test_address = Address(number=432,
                               street='rue du rat',
                               city='Montargis',
                               state='Loiret',
                               zip_code='45200',
                               country_iso_code='FR')
        test_address.save()
        title = "test-letting"
        letting = Letting(title=title, address=test_address)
        letting.save()
        uri = reverse('letting', kwargs={'letting_id': letting.id})
        response = self.client.get(uri)
        assert response.status_code == 200
        assert b'<title>test-letting</title>' in response.content
