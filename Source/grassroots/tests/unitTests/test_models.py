from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from ...forms import UserRegistrationForm

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view_post_valid_form(self):
        form_data = {
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
            'first_name': 'Test',
            'last_name': 'User',
            'address': '11 Upper St',
            'phone': '1234567890',
        }
        response = self.client.post(reverse('register'), data=form_data, follow=True)

        # Check the response content for debugging purposes
        print(response.content)

        # Check that the response is a redirect
        self.assertRedirects(response, reverse('home'), status_code=200)  # Change to 200 as we're following the redirect

         # Check that the user is redirected to the 'home' view
        self.assertEqual(response.status_code, 200)

        # Check that a new user is created in the database
        new_user = get_user_model().objects.get(email='testuser@example.com')
        self.assertIsNotNone(new_user)
        self.assertTrue(new_user.check_password('password123'))

        # Check that the user is logged in
        self.assertTrue(response.client.session['_auth_user_id'])


    def test_register_view_post_invalid_form(self):
        form_data = {
            'email': '',  # Invalid email to trigger form validation error
            'password1': 'password',
            'password2': 'password',
        }
        response = self.client.post(reverse('register'), data=form_data)

        # Check that the response is not a redirect
        self.assertEqual(response.status_code, 200)

        # Check that the form is displayed with errors
        self.assertContains(response, 'This field is required.')  # Check for the expected form error

        # Check that no new user is created in the database
        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(email='')

        # Check that the user is not logged in
        self.assertFalse(response.client.session.get('_auth_user_id'))
