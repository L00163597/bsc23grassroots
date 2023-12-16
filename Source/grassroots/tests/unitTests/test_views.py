from django.test import TestCase
from django.urls import reverse


# unit test for "register" view in the Source/grassroots/views.py
# "register" view is supposed to redirect the user to "home" page upon successful login
class RegisterViewTest(TestCase):
    # specifically deals with POST request
    def test_register_view_post_request(self):
        # arrange the data for POST request
        data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',
            'address': '123 Test St',
            'password': 'password123',
        }
        # create a POST request to "register" view
        response = self.client.post(reverse('register'), data)

        # check if the user is redirected to home page upon successful login
        self.assertRedirects(response, reverse('home'))
