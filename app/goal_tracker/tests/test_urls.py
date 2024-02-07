from django.test import SimpleTestCase
from django.contrib.auth import views as auth_views
from django.urls import reverse, resolve

from .. import views


class TestUrls(SimpleTestCase):

    def test_if_login_url_runs_correct_view(self):
        url = '/login/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.LoginView)

    def test_if_login_url_name_runs_correct_view(self):
        url = reverse('login')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.LoginView)

    def test_if_logout_url_runs_correct_view(self):
        url = '/logout/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.LogoutView)

    def test_if_logout_url_name_runs_correct_view(self):
        url = reverse('logout')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.LogoutView)

    def test_if_password_reset_url_runs_correct_view(self):
        url = '/password-reset/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetView)

    def test_if_password_reset_url_name_runs_correct_view(self):
        url = reverse('password_reset')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetView)

    def test_if_password_reset_done_url_runs_correct_view(self):
        url = '/password-reset/done/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetDoneView)

    def test_if_password_reset_done_url_name_runs_correct_view(self):
        url = reverse('password_reset_done')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetDoneView)

    def test_if_password_reset_confirm_url_runs_correct_view(self):
        url = '/password-reset-confirm/<uidb64>/<token>/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetConfirmView)

    def test_if_password_reset_confirm_url_name_runs_correct_view(self):
        url = reverse('password_reset_confirm', args=['uidb64', 'some_token'])
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetConfirmView)

    def test_if_password_reset_complete_url_runs_correct_view(self):
        url = '/password-reset-complete/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetCompleteView)

    def test_if_password_reset_complete_url_name_runs_correct_view(self):
        url = reverse('password_reset_complete')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, auth_views.PasswordResetCompleteView)

    def test_if_update_user_url_runs_correct_view(self):
        url = '/update_user/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.update_user)

    def test_if_update_user_url_name_runs_correct_view(self):
        url = reverse('update-user')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.update_user)

    def test_if_register_url_runs_correct_view(self):
        url = '/register/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.register_user)

    def test_if_register_url_name_runs_correct_view(self):
        url = reverse('register')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.register_user)
