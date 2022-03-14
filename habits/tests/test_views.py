from django.test import TestCase, Client
from django.utils.timezone import datetime, make_aware
from django.urls import reverse
from django.contrib.auth.models import User

from habits.views import list_habits
from habits.models import Habit


class ListHabitsTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='testing321')
        self.client = Client()

        start_date = datetime(2022, 3, 13, 0, 0, 0)
        Habit.objects.create(
            name='Alcohol',
            owner=self.user,
            start_date=make_aware(start_date),
            reason='It is bad for life.'
        )

        Habit.objects.create(
            name='Sweets',
            owner=self.user,
            start_date=make_aware(start_date),
            reason='Get ready for summer.'
        )

    def test_list_habits_method_with_logged_out_user(self):

        response = self.client.get(reverse('habits:list-habits'))

        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(response.resolver_match.func, list_habits)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/my_habits/')

    def test_list_habits_method_with_logged_in_user(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.get(reverse('habits:list-habits'))

        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(response.resolver_match.func, list_habits)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/habits_list.html')

    def test_if_list_habits_method_returns_correct_queryset(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.get(reverse('habits:list-habits'))
        queryset = Habit.objects.filter(owner=self.user).order_by('start_date')

        self.assertQuerysetEqual(response.context['objects'], queryset)
