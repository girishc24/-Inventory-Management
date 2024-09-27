from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Item

class ItemTests(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

       
        self.item = Item.objects.create(name="Test Item", description="Test Description")
        self.url = reverse('item_detail', args=[self.item.id])

    def authenticate(self):
        """Helper method to include JWT token in the headers"""
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.access_token)

    def test_get_item(self):
        
        self.authenticate()
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_get_non_existent_item(self):
        
        self.authenticate()
        
        url = reverse('item_detail', args=[999])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
