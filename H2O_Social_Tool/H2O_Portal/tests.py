from django.test import TestCase
from django.urls import reverse, resolve
from .views import *

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
    
    def test_view_list(self):
        array = ['signup','managecreds','listscheduled', 'listcompleted' ]
        length = len(array)
        for i in range(length):
            def test_item_view_status_code(self):
                url = reverse(array[i])
                response = self.client.get(url)
                self.assertEquals(response.status_code, 200)
            
            def test_item_url_resolves_item_view(self):
                view = resolve('/'+ array[i] + '/')
                self.assertEquals(view.func, array[i])            
    # #Signup
    # def test_signup_view_status_code(self):
    #     url = reverse('signup')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_signup_url_resolves_signup_view(self):
    #     view = resolve('/signup/')
    #     self.assertEquals(view.func, signup)

    # #Managecredentials
    # def test_managecreds_view_status_code(self):
    #     url = reverse('managecreds')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_managecreds_url_resolves_managecreds_view(self):
    #     view = resolve('/managecreds/')
    #     self.assertEquals(view.func, managecreds)

    # #List scheduled
    # def test_listscheduled_view_status_code(self):
    #     url = reverse('listscheduled')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_listscheduled_url_resolves_listscheduled_view(self):
    #     view = resolve('/listscheduled/')
    #     self.assertEquals(view.func, listscheduled)

    # #List completed
    # def test_listcompleted_view_status_code(self):
    #     url = reverse('listcompleted')
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    # def test_listcompleted_url_resolves_listcompleted_view(self):
    #     view = resolve('/listcompleted/')
    #     self.assertEquals(view.func, listcompleted)
