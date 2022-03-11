from django.test import TestCase
from django.contrib.auth.models import User

from habits.models import Habit, Milestone


class HabitTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='testing321')
        self.milestone = Milestone.objects.create(name='One Month')
        self.habit = Habit.objects.create(
            name='Alco',
            owner=self.user,
            milestone=self.milestone
        )

    def test_some(self):
        print(self.habit.start_date)