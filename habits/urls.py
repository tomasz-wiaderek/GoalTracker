from django.urls import path

from . import views


app_name = 'habits'
urlpatterns = [
    path('my_habits/', views.list_habits, name='list-habits'),
]
