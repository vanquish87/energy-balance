from django.test import TestCase
from django.urls import reverse
from account.models import Account
from .models import Weight

class CreateEntryTests(TestCase):
    def setUp(self):
        # create a user and log them in
        self.user = Account.objects.create_user(
            email='testuser@test.com', password='testpass', first_name='test', last_name='now', username='testing')
        self.client.login(email='testuser@test.com', password='testpass')

    def test_form_displayed_correctly(self):
        response = self.client.get(reverse('create-entry'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_form_submission_saves_to_database(self):
        # log in as the user
        self.client.login(email='testuser@test.com', password='testpass')

        data = {'weight': 70, 'calorie_intake': 2000, 'date': '2022-01-01'}
        response = self.client.post(reverse('create-entry'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Weight.objects.count(), 1)
        
        weight = Weight.objects.first()
        self.assertEqual(weight.weight, 70)
        self.assertEqual(weight.calorie_intake, 2000)
        self.assertEqual(weight.date, '2022-01-01')
        self.assertEqual(weight.user, self.user)

    def test_form_submission_with_invalid_data_displays_error(self):
        data = {'weight': -70, 'calorie_intake': 2000, 'date': '2022-01-01'}
        response = self.client.post(reverse('create-entry'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'error')
        self.assertEqual(Weight.objects.count(), 0)

    def test_form_submission_redirects_to_profile(self):
        data = {'weight': 70, 'calorie_intake': 2000, 'date': '2022-01-01'}
        response = self.client.post(reverse('create-entry'), data)
        self.assertRedirects(response, reverse('profile'))
