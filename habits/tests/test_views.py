from django.test import TestCase, Client
from django.utils.timezone import datetime, make_aware
from django.urls import reverse
from django.contrib.auth.models import User

from habits import views
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

        response = self.client.get(reverse('habits:list'))

        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(response.resolver_match.func, views.list_habits)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/my_habits/list/')

    def test_list_habits_method_with_logged_in_user(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.get(reverse('habits:list'))

        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(response.resolver_match.func, views.list_habits)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/list.html')

    def test_if_list_habits_method_returns_correct_queryset(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.get(reverse('habits:list'))
        queryset = Habit.objects.filter(owner=self.user).order_by('start_date')

        self.assertQuerysetEqual(response.context['objects'], queryset)


class CreateHabitTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='testing321')
        start_date = datetime(2022, 3, 13, 0, 0, 0)
        self.data = {
            'name': 'Sweets',
            'owner': self.user,
            'start_date': make_aware(start_date),
            'reason': 'It is bad for life.'

        }
        self.client = Client()

    def test_if_create_habit_POST_view_creates_new_habit(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('habits:create'), data=self.data)

        new_habit = Habit.objects.get(name='Sweets')

        self.assertEqual(new_habit.name, self.data['name'])
        self.assertEqual(new_habit.owner, self.data['owner'])
        self.assertEqual(new_habit.start_date, self.data['start_date'])
        self.assertEqual(new_habit.reason, self.data['reason'])

    def test_create_habit_POST_view(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('habits:create'), data=self.data)

        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.resolver_match.func, views.create_habit)
        self.assertEqual(response.status_code, 302)

    def test_if_create_habit_POST_view_redirects_correctly(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('habits:create'), data=self.data)

        self.assertRedirects(response, '/my_habits/list/')

    def test_create_habit_POST_view_as_unlogged_user(self):

        response = self.client.post(reverse('habits:create'), data=self.data)

        queryset = Habit.objects.all()

        self.assertQuerysetEqual(queryset, [])
        self.assertRedirects(response, '/login/?next=/my_habits/create/')
        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.resolver_match.func, views.create_habit)
        self.assertEqual(response.status_code, 302)


class UpdateHabitTest(TestCase):

    def setUp(self):

        self.user_owner = User.objects.create_user(username='TestUser', password='testing321')
        self.user = User.objects.create_user(username='TestUser2', password='testing321')
        start_date = datetime(2022, 3, 13, 0, 0, 0)
        Habit.objects.create(
            name='Alcohol',
            owner=self.user_owner,
            start_date=make_aware(start_date),
            reason='It is bad for life.'
        )
        self.habit = Habit.objects.get(owner=self.user_owner)
        self.data = {
            'name': 'New name',
            'reason': 'New reason'
        }
        self.client = Client()

    def test_if_another_user_cant_update_someones_habit(self):

        self.client.login(username='TestUser2', password='testing321')
        response = self.client.post(reverse('habits:update', args=[self.habit.pk]), data=self.data)

        self.assertNotEqual(self.habit.name, self.data['name'])
        self.assertNotEqual(self.habit.reason, self.data['reason'])
        self.assertRedirects(response, '/login/')
        self.assertEqual(response.status_code, 302)

    def test_if_update_habit_POST_view_updates_habit(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('habits:update', args=[self.habit.pk]), data=self.data)

        updated_habit = Habit.objects.get(owner=self.user_owner)

        self.assertEqual(updated_habit.name, self.data['name'])
        self.assertEqual(updated_habit.reason, self.data['reason'])

    def test_update_habit_POST_view(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('habits:update', args=[self.habit.pk]), data=self.data)

        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.resolver_match.func, views.update_habit)
        self.assertEqual(response.status_code, 302)

    def test_if_update_habit_POST_view_redirects_correctly(self):

        self.client.login(username='TestUser', password='testing321')
        response = self.client.post(reverse('habits:update', args=[self.habit.pk]), data=self.data)

        self.assertRedirects(response, '/my_habits/list/')

    def test_update_habit_POST_view_as_unlogged_user(self):

        response = self.client.post(reverse('habits:update', args=[self.habit.pk]), data=self.data)

        self.assertNotEqual(self.habit.name, self.data['name'])
        self.assertNotEqual(self.habit.reason, self.data['reason'])
        self.assertRedirects(response, '/login/?next=/my_habits/update/1/')
        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(response.resolver_match.func, views.update_habit)
        self.assertEqual(response.status_code, 302)
