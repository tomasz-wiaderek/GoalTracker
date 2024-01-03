
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import register_user, update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('my_habits/', include('habits.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', next_page='pages:home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register_user, name='register'),
    path('update_user/', update_user, name='update-user'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
