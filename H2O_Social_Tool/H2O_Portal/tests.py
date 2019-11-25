from django.test import TestCase
from django.urls import reverse, resolve
from .views import home

# Create your tests here.
class TestUrls(TestCase):
    #home url
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    # #Signup
    # def test_signup_view_status_code(self):
    #     url = reverse('signup')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_signup_url_resolves_signup_view(self):
    #     view = resolve('signup/')
    #     self.assertEquals(view.func, signup)

    # #Login
    # def test_loginuser_view_status_code(self):
    #     url = reverse('loginuser')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_loginuser_url_resolves_loginuser_view(self):
    #     view = resolve('loginuser/')
    #     self.assertEquals(view.func, loginuser)

    # #Managecredentials
    # def test_managecreds_view_status_code(self):
    #     url = reverse('managecreds')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_managecreds_url_resolves_managecreds_view(self):
    #     view = resolve('managecreds/')
    #     self.assertEquals(view.func, managecreds)

    # #List scheduled
    # def test_listscheduled_view_status_code(self):
    #     url = reverse('listscheduled')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_listscheduled_url_resolves_listscheduled_view(self):
    #     view = resolve('listscheduled/')
    #     self.assertEquals(view.func, listscheduled)

    # #List completed
    # def test_listcompleted_view_status_code(self):
    #     url = reverse('listcompleted')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_listcompleted_url_resolves_listcompleted_view(self):
    #     view = resolve('listcompleted/')
    #     self.assertEquals(view.func, listcompleted)
