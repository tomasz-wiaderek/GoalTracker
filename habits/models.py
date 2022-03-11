from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Sentance(models.Model):
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.content


class Milestone(models.Model):
    name = models.CharField(max_length=128)
    req_abstynence_time = models.DurationField(blank=True)
    icon = models.ImageField(upload_to='icons/milestones/', default='icon.jpg')
    is_achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Habit(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=now())
    reason = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    def get_abstynance_time(self):
        return now() - self.start_date
