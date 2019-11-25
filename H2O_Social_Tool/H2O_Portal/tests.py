from django.test import TestCase
from django.urls import reverse, resolve
from .views import home

# Create your tests here.
class TestUrls(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)