from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Pins, Lists
from rest_framework.test import APIRequestFactory

# Create your tests here.

test_user1 = {
            "usename": "test_user1",
            "email": "whatever@whatever1.com",
            "password": "top_secret"
}

test_user2 = {
            "usename": "test_user2",
            "email": "whatever@whatever2.com",
            "password": "teehehe2"
}

class SimpleTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(test_user1)
        
        # cls.pin = Pins.objects.create(test_pin1)
        # cls.list = Lists.objects.create(test_list1)
        # cls.user = User.objects.create_user(test_user1)
    
    def test_details(self):
        request = self.factory.get('/users')
        request.user = self.user
        # response = my_view(request)