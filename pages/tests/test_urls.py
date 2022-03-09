from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages import views


class PagesUrls(SimpleTestCase):

    def test_if_home_url_runs_correct_view(self):
        url = '/home/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.home)

    def test_if_home_name_runs_correct_view(self):
        url = reverse('pages:home')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.home)
