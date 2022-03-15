from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitCreateForm, HabitUpdateForm


@login_required(login_url='login')
def list_habits(request):
    habits = Habit.objects.filter(owner=request.user).order_by('start_date')
    return render(request, template_name='habits/list.html', context={'objects': habits})


@login_required(login_url='login')
def create_habit(request):
    if request.method == 'POST':
        form = HabitCreateForm(request.POST)
        if form.is_valid():
            form.cleaned_data['owner'] = request.user
            Habit.objects.create(**form.cleaned_data)
            return redirect('habits:list')
    else:
        form = HabitCreateForm()
    return render(request, template_name='habits/create.html', context={'form': form})


@login_required(login_url='login')
def update_habit(request, pk):
    habit = Habit.objects.get(pk=pk)
    if habit.owner == request.user:
        if request.method == 'POST':
            form = HabitUpdateForm(request.POST, instance=habit)
            if form.is_valid():
                form.save()
                return redirect('habits:list')
        else:
            form = HabitUpdateForm(instance=habit)
    else:
        return redirect('login')
    return render(request, template_name='habits/update.html', context={'form': form})


