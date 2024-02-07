from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .. import views


class HomeViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('pages:home'))

    def test_if_given_url_runs_correct_view(self):
        self.assertEqual(self.response.resolver_match.func, views.home)

    def test_if_response_status_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_if_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')


class AboutViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('pages:about'))

    def test_if_given_url_runs_correct_view(self):
        self.assertEqual(self.response.resolver_match.func, views.about)

    def test_if_response_status_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_if_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'pages/about.html')
