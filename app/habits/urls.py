from django.urls import path

from . import views


app_name = 'habits'
urlpatterns = [
    path('list/', views.list_habits, name='list'),
    path('create/', views.create_habit, name='create'),
    path('update/<int:pk>/', views.update_habit, name='update'),
    path('reset/<int:pk>/', views.reset_habit, name='reset'),
    path('delete/<int:pk>/', views.delete_habit, name='delete'),
]
