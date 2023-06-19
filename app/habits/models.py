from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from .initials import init_list


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
        return Milestone.objects.get(habit__pk=self.pk, is_active=True)

    def get_all_milestones(self):
        return Milestone.objects.filter(habit__pk=self.pk).order_by('req_abstynence_time')

    def get_all_achieved_milestones(self):
        return Milestone.objects.filter(habit__pk=self.pk, is_achieved=True).order_by('req_abstynence_time')

    def init_milestones(self):
        for m in init_list:
            Milestone.objects.create(name=m.get('name'),
                                     req_abstynence_time=m.get('req_abstynence_time'),
                                     is_active=m.get('is_active'),
                                     habit=self)

    def delete_all_milestones(self):
        self.get_all_milestones().delete()

    def scan_and_update_milestones(self):
        milestones = self.get_all_milestones()
        for m in range(0, len(milestones)):
            milestones[m].update_status()
            if milestones[m].is_achieved and m < len(milestones) - 1:
                milestones[m + 1].is_active = True
                milestones[m + 1].save()


class Milestone(models.Model):
    name = models.CharField(max_length=128)
    req_abstynence_time = models.DurationField(null=True)
    is_achieved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_finished = models.DateTimeField(null=True, blank=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def update_status(self):
        end_date = self.habit.start_date + self.req_abstynence_time
        if now() > end_date:
            self.is_achieved = True
            self.is_active = False
            self.date_finished = end_date
            self.save()
