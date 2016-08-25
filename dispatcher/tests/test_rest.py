from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework import status

from .base import BaseTestCars

# class RestCarTest(BaseTestCars, APITestCase):
class RestCarTest(BaseTestCars,APITestCase):
    def test_get_cars_without_loging(self):   
        response = self.client.get('/api/v1/cars/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_get_cars_loging_as_dispatcher(self):   
        login = self.client.login(username='dispatcher', password='123')     
        response = self.client.get('/api/v1/cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/v1/automodels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/v1/automarks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cars_loging_as_customUser(self):   
        login = self.client.login(username='custom', password='123')     
        response = self.client.get('/api/v1/cars/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

