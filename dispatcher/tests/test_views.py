from django.test import TestCase

from .base import BaseTestCars
class DispatcherPageTest(BaseTestCars):

    def test_login(self):
        login = self.client.login(username='dispatcher', password='123') 
        self.assertTrue(login)              
        response = self.client.get('/dispatcher/')
        self.assertEqual(response.status_code, 200)      
        self.client.logout() 

    def test_login_no_dispatcher(self):
        self.client.login(username='custom', password='123') 
        response = self.client.get('/dispatcher/')
        self.assertNotEqual(response.status_code, 200)
        

    def test_dispatcher_page_renders(self):
        self.client.login(username='dispatcher', password='123') 
        response = self.client.get('/dispatcher/')
        self.assertTemplateUsed(response, 'dispatcher/dispatcher.html')
        self.client.logout() 
