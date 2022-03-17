from django.test import TestCase, Client
from django.contrib.auth.models import User
from habits import forms


class HabitCreateFormTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(username='TestUser', password='testing321')

        self.data = {
            'name': ' Test Habit ',
            'owner': self.user,
            'start_date': '2022-03-01 00:00',
            'reason': ' This is test case reason. '
        }

    def test_HabitCreateForm_is_valid(self):

        form = forms.HabitCreateForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_HabitCreateForm_missing_name(self):

        self.data['name'] = None
        form = forms.HabitCreateForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_HabitCreateForm_missing_start_date(self):

        self.data['start_date'] = None
        form = forms.HabitCreateForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_HabitCreateForm_missing_reason(self):

        self.data['reason'] = None
        form = forms.HabitCreateForm(data=self.data)

        self.assertFalse(form.is_valid())


class HabitUpdateFormTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(username='TestUser', password='testing321')

        self.data = {
            'name': ' Test Habit ',
            'reason': ' This is test case reason. '
        }

    def test_HabitUpdateForm_is_valid(self):

        form = forms.HabitUpdateForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_HabitUpdateForm_missing_name(self):

        self.data['name'] = None
        form = forms.HabitUpdateForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_HabitUpdateForm_missing_reason(self):

        self.data['reason'] = None
        form = forms.HabitUpdateForm(data=self.data)

        self.assertFalse(form.is_valid())


class HabitResetForm(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(username='TestUser', password='testing321')

        self.data = {
            'start_date': '2022-03-01 00:00',
        }

    def test_HabitResetForm_is_valid(self):

        form = forms.HabitResetForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_HabitResetForm_missing_name(self):

        self.data['start_date'] = None
        form = forms.HabitResetForm(data=self.data)

        self.assertFalse(form.is_valid())
