from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from goal_tracker.forms import UserRegisterForm, UserUpdateForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Witaj {username}! Twoje konto zostało utworzone. Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='login')
def update_user(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Twój profil został zaktualizowany.')
            return redirect('update-user')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form': user_form,
    }
    return render(request, 'users/update.html', context=context)
