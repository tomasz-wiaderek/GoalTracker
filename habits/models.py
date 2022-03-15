from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Sentance(models.Model):
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.content


class Habit(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_abstynance_time(self):
        return now() - self.start_date

    def get_current_milestone(self):
        return Milestone.objects.get(is_achieved=False, habit__pk=self.pk)

    def get_all_milestones(self):
        return Milestone.objects.filter(habit__pk=self.pk).order_by('-date_finished')


class Milestone(models.Model):
    name = models.CharField(max_length=128)
    req_abstynence_time = models.DurationField(null=True)
    icon = models.ImageField(upload_to='icons/milestones/', default='icon.jpg')
    is_achieved = models.BooleanField(default=False)
    date_finished = models.DateTimeField(null=True, blank=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def set_is_achieved_true(self):
        end_date = self.habit.start_date + self.req_abstynence_time
        if now() >= end_date:
            self.is_achieved = True
            self.date_finished = end_date