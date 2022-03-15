from django.test import SimpleTestCase
from django.urls import resolve, reverse

from habits import views


class TestUrls(SimpleTestCase):

    def test_if_list_url_runs_correct_view(self):
        url = '/my_habits/list/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.list_habits)

    def test_if_list_url_name_runs_correct_view(self):
        url = reverse('habits:list')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.list_habits)

    def test_if_create_url_runs_correct_view(self):
        url = '/my_habits/create/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.create_habit)

    def test_if_create_url_name_runs_correct_view(self):
        url = reverse('habits:create')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.create_habit)
