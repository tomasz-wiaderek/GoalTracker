from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from ..views import register_user, update_user


class RegisterUserTest(TestCase):

    def setUp(self):

        self.data = {
            'username': 'TestUser',
            'email': 'testuser@mail.com',
            'password1': 'testing321',
            'password2': 'testing321'
        }

        self.client = Client()

    def test_register_user_GET_view(self):

        response = self.client.get(reverse('register'))

        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(response.resolver_match.func, register_user)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_user_POST_view(self):

        response = self.client.post(reverse('register'), data=self.data)

        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.resolver_match.func, register_user)
        self.assertEqual(response.status_code, 302)

    def test_if_register_user_POST_view_creates_new_user(self):

        self.client.post(reverse('register'), data=self.data)
        created_user = User.objects.get(username='TestUser')

        self.assertEqual(created_user.username, self.data['username'])
        self.assertEqual(created_user.email, self.data['email'])

    def test_if_register_user_POST_view_redirects_correctly(self):

        response = self.client.post(reverse('register'), data=self.data)

        self.assertRedirects(response, '/login/')


class UpdateUserTest(TestCase):

    def setUp(self):

        self.data = {
            'username': 'TestUser',
            'email': 'testuser@mail.com',
            'password1': 'testing321',
            'password2': 'testing321'
        }

        self.new_data = {
            'username': 'TestUserEditedName',
            'email': 'editedmail@mail.com'
        }
        User.objects.create_user(username='TestUser', password='testing321')
        self.client = Client()

    def test_update_user_GET_view_as_unlogged_user(self):

        response = self.client.get(reverse('update-user'))

        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(response.resolver_match.func, update_user)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=%2Fupdate_user%2F')

    def test_update_user_POST_view_as_unlogged_user(self):

        response = self.client.post(reverse('update-user'), data=self.data)

        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.resolver_match.func, update_user)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=%2Fupdate_user%2F')

    def test_if_update_user_POST_view_updates_logged_in_users_data(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('update-user'), self.new_data)

        updated_user = User.objects.get(username=self.new_data['username'])

        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('update-user'))
        self.assertEqual(response.resolver_match.func, update_user)
        self.assertEqual(updated_user.username, self.new_data['username'])
        self.assertEqual(updated_user.email, self.new_data['email'])
