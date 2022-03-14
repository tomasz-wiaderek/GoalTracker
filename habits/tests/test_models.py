from django.test import TestCase
from django.contrib.auth.models import User
import django.utils.timezone as tz
from django.utils.timezone import make_aware

from habits.models import Habit, Milestone


class HabitTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='testing321')
        self.milestone = Milestone.objects.create(name='One Week', req_abstynence_time=tz.timedelta(days=7))

        start_date = tz.datetime(2022, 3, 13, 0, 0, 0)
        self.habit = Habit.objects.create(
            name='Alco',
            owner=self.user,
            milestone=self.milestone,
            start_date=make_aware(start_date),
            reason='It is bad for live.'
        )

    def test_if_habit_get_abstynance_time_is_timedelta(self):

        self.assertIsInstance(self.habit.get_abstynance_time(), tz.timedelta)


class MilestoneTest(TestCase):

    def setUp(self):

        self.milestone = Milestone.objects.create(
            name='One week',
            req_abstynence_time=tz.timedelta(days=7)
        )

    def test_some(self):
        print(type(self.milestone.req_abstynence_time))
        print(self.milestone.req_abstynence_time)
