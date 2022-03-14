from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import Habit


@login_required(login_url='login')
def list_habits(request):
    habits = Habit.objects.filter(owner=request.user).order_by('start_date')
    context = {'objects': habits}
    return render(request, template_name='habits/habits_list.html', context=context)
