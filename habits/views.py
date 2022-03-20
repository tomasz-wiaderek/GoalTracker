from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitCreateForm, HabitUpdateForm, HabitResetForm


@login_required(login_url='login')
def list_habits(request):
    habits = Habit.objects.filter(owner=request.user).order_by('start_date')
    for h in habits:
        h.scan_and_update_milestones()
    return render(request, template_name='habits/list.html', context={'objects': habits})


@login_required(login_url='login')
def create_habit(request):
    if request.method == 'POST':
        form = HabitCreateForm(request.POST)
        if form.is_valid():
            form.cleaned_data['owner'] = request.user
            habit = Habit.objects.create(**form.cleaned_data)
            habit.save()
            habit.init_milestones()
            habit.scan_and_update_milestones()
            return redirect(reverse('habits:list'))
    else:
        form = HabitCreateForm()
    return render(request, template_name='habits/create.html', context={'form': form})


@login_required(login_url='login')
def update_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if habit.owner == request.user:
        if request.method == 'POST':
            form = HabitUpdateForm(request.POST, instance=habit)
            if form.is_valid():
                form.save()
                return redirect(reverse('habits:list'))
        else:
            form = HabitUpdateForm(instance=habit)
    else:
        return redirect('login')
    return render(request, template_name='habits/update.html', context={'form': form})


@login_required(login_url='login')
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if habit.owner == request.user:
        if request.method == 'POST':
            habit.delete()
            return redirect(reverse('habits:list'))
    else:
        return redirect('login')
    return render(request, template_name='habits/delete.html', context={'object': habit})


@login_required(login_url='login')
def reset_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if habit.owner == request.user:
        if request.method == 'POST':
            form = HabitResetForm(request.POST, instance=habit)
            if form.is_valid():
                form.save()
                habit.delete_all_milestones()
                habit.init_milestones()
                habit.scan_and_update_milestones()
                return redirect(reverse('habits:list'))
        else:
            form = HabitResetForm(instance=habit)
    else:
        return redirect('login')
    return render(request, template_name='habits/reset.html', context={'form': form})
