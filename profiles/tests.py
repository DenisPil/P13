from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse


class TestProfiles(TestCase):

    def test_profiles_page(self):
        path = reverse("profiles_index")
        response = self.client.get(path)
        assert response.status_code == 200 and \
            b'<h1>Profiles</h1>' \
            in response.content

    def test_letting_detail(self):
        username = "user"
        user = User(username=username)
        user.save()
        profile = Profile(user_id=user.id)
        profile.save()
        path = reverse('profile', kwargs={'username': user.username})
        response = self.client.get(path)
        assert response.status_code == 200 and \
            b'<title>user</title>' \
            in response.content
