from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import timedelta, datetime, make_aware, now

from habits.models import Habit, Milestone
from habits.initials import init_list


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
                                                   is_achieved=True,
                                                   habit=self.habit)

        self.milestone3 = Milestone.objects.create(name='week',
                                                   req_abstynence_time=timedelta(weeks=1),
                                                   is_achieved=False,
                                                   is_active=True,
                                                   habit=self.habit)

    def test_if_init_milestones_method_creates_initial_mileston(self):

        start_date = datetime(2022, 3, 1, 0, 0, 0)
        habit = Habit.objects.create(
            name='Alco',
            owner=self.user,
            start_date=make_aware(start_date),
            reason='It is bad for life.'
        )

        habit.init_milestones()
        self.assertEqual(len(habit.get_all_milestones()), len(init_list))

    def test_if_get_abstynance_time_is_timedelta(self):

        self.assertIsInstance(self.habit.get_abstynance_time(), timedelta)

    def test_if_get_abstynance_time_returns_correct_time(self):
        period = now() - make_aware(datetime(2022, 3, 13, 0, 0, 0))

        self.assertEqual(self.habit.get_abstynance_time(), period)

    def test_if_get_current_milestone_returns_active_milestone(self):

        self.assertIsInstance(self.habit.get_current_milestone(), Milestone)
        self.assertEqual(self.habit.get_current_milestone(), self.milestone3)

    def test_if_get_all_milestones_returns_correct_queryset(self):

        queryset = Milestone.objects.filter(habit__pk=self.habit.pk).order_by('req_abstynence_time')

        self.assertQuerysetEqual(queryset, self.habit.get_all_milestones())

    def test_if_delete_all_milestones_deletes_habits_milestones(self):

        self.habit.delete_all_milestones()

        self.assertQuerysetEqual(self.habit.get_all_milestones(), [])


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

    def test_if_update_status_method_updates_field_when_abstynence_time_achieved(self):

        self.milestone2.update_status()

        self.assertTrue(self.milestone2.is_achieved)
        self.assertFalse(self.milestone2.is_active)

    def test_if_update_status_method_dont_updates_field_when_abstynence_time_not_achieved(self):

        self.milestone3.update_status()

        self.assertFalse(self.milestone3.is_achieved)


class StartTimerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='TestUser', password='testing321')
        self.habit = Habit.objects.create(
            name='Alcohol',
            owner=self.user,
            start_date=make_aware(datetime(2022, 3, 18, 16, 0, 0)),
            reason='It is bad for life.'
        )

    def test_timer(self):
        self.milestone5 = Milestone.objects.create(name='One Day',
                                                   req_abstynence_time=timedelta(minutes=11),
                                                   is_achieved=False,
                                                   habit=self.habit)
        self.milestone5.start_timer()
