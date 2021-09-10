from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Pins, Lists
from rest_framework.test import APIRequestFactory

test_pin1 = {
            "pin_id": 50,
            "name": "test_location1",
            "lat": "51.5697586000",
            "lng": "-0.0845718000",
            "notes": "I'd like to visit test location1",
            "colour": "#ff006e",
            "user_id": 1
        }

test_pin2 = {
            "pin_id": 51,
            "name": "test_location2",
            "lat": "51.5697586000",
            "lng": "-0.0845718000",
            "notes": "I'd like to visit test location2",
            "colour": "#ff006e",
            "user_id": 2
        }

test_list1 = {
            "name": "test_list1",
            "thumb": "test thumb1",
            "colour": "#dd3344",
            "list_pins": [1,2,3],
            "user_id": 3
}

test_list2 = {
            "name": "test_list2",
            "thumb": "test thumb2",
            "colour": "#dd4433",
            "list_pins": [4,6,8],
            "user_id": 4
}

#maybe try using pins_router as the view?

factory = APIRequestFactory() 

request = factory.post('/api/pins/', test_pin1, format='json')

class SimpleTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(test_user1)

        # cls.pin = Pins.objects.create(test_pin1)
        # cls.list = Lists.objects.create(test_list1)
        # cls.user = User.objects.create_user(test_user1)
    
    def test_details(self):
        request = self.factory.get('/users')
        request.user = self.user
        # response = my_view(request)
