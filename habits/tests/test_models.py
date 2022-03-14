from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import timedelta, datetime, make_aware

from habits.models import Habit, Milestone


class HabitTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='testing321')

        start_date = datetime(2022, 3, 13, 0, 0, 0)
        self.habit = Habit.objects.create(
            name='Alcohol',
            owner=self.user,
            start_date=make_aware(start_date),
            reason='It is bad for life.'
        )

        self.milestone1 = Milestone.objects.create(name='One Day',
                                                   req_abstynence_time=timedelta(days=1),
                                                   is_achieved=True,
                                                   date_finished=make_aware(datetime(2022, 3, 14, 0, 0, 0)),
                                                   habit=self.habit)

        self.milestone2 = Milestone.objects.create(name='Three Days',
                                                   req_abstynence_time=timedelta(days=3),
                                                   is_achieved=False,
                                                   habit=self.habit)

    def test_if_get_abstynance_time_is_timedelta(self):

        self.assertIsInstance(self.habit.get_abstynance_time(), timedelta)

    def test_if_get_current_milestone_returns_active_milestone(self):

        self.assertIsInstance(self.habit.get_current_milestone(), Milestone)
        self.assertEqual(self.habit.get_current_milestone(), self.milestone2)

    def test_if_get_all_milestones_returns_correct_queryset(self):

        queryset = Milestone.objects.filter(habit__pk=self.habit.pk).order_by('-date_finished')

        self.assertQuerysetEqual(queryset, self.habit.get_all_milestones())


class MilestoneTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='TestUser', password='testing321')

        start_date = datetime(2022, 3, 1, 0, 0, 0)
        self.habit = Habit.objects.create(
            name='Alcohol',
            owner=self.user,
            start_date=make_aware(start_date),
            reason='It is bad for life.'
        )

        self.milestone1 = Milestone.objects.create(name='One Day',
                                                   req_abstynence_time=timedelta(days=1),
                                                   is_achieved=True,
                                                   date_finished=make_aware(datetime(2022, 3, 2, 0, 0, 0)),
                                                   habit=self.habit)

        self.milestone2 = Milestone.objects.create(name='Three Days',
                                                   req_abstynence_time=timedelta(days=3),
                                                   is_achieved=False,
                                                   habit=self.habit)

        self.milestone3 = Milestone.objects.create(name='One Month',
                                                   req_abstynence_time=timedelta(days=30),
                                                   is_achieved=False,
                                                   habit=self.habit)

    def test_if_method_set_is_achieved_true_updates_field_when_abstynence_time_achieved(self):

        self.milestone2.set_is_achieved_true()

        self.assertTrue(self.milestone2.is_achieved)

    def test_if_method_set_is_achieved_true_dont_updates_field_when_abstynence_time_not_achieved(self):

        self.milestone3.set_is_achieved_true()

        self.assertFalse(self.milestone3.is_achieved)
