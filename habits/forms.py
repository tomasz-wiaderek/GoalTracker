from django import forms
from .models import Habit


class HabitCreateForm(forms.ModelForm):
    name = forms.CharField(strip=True)
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%y-%m-%d %H:%M', attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))

    class Meta:
        model = Habit
        fields = ['name', 'start_date', 'reason']


class HabitUpdateForm(forms.ModelForm):
    name = forms.CharField(strip=True)
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))

    class Meta:
        model = Habit
        fields = ['name', 'reason']


class HabitResetForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%y-%m-%d %H:%M', attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))

    class Meta:
        model = Habit
        fields = ['start_date']
