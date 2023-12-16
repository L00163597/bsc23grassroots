from django.test import TestCase
from ...forms import UserRegistrationForm


class MyTest(TestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)


class UserRegistrationFormTest(TestCase):

    def test_user_registration_form_validation(self):
        # Test the form with valid data
        valid_form_data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',
            'address': '123 Test St',
            'password': 'password123',
        }
        form = UserRegistrationForm(data=valid_form_data)
        self.assertTrue(form.is_valid())

        # Test the form with invalid data (missing first name)
        invalid_form_data = valid_form_data.copy()
        invalid_form_data['first_name'] = ''
        form = UserRegistrationForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
