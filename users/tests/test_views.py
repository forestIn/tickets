from django.test import TestCase
from users.models import CustomUser

class UsersPageTest(TestCase):

    @classmethod
    def setUpTestData(cls):    
        u=CustomUser(username='Test', email="Anikjev@gmail.com", is_active=True)
        u.set_password('123')
        u.save()

    def test_login(self):
        login = self.client.login(username='Test', password='123') 
        self.assertTrue(login)      
        self.client.logout() 
        response = self.client.get('/users/update/')
        self.assertEqual(response.status_code, 302)
        


    def test_users_page_renders(self):
        self.client.login(username='Test', password='123') 
        response = self.client.get('/users/update/')
        self.assertTemplateUsed(response, 'users/customuser_form.html')
        self.client.logout() 