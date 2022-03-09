from django.shortcuts import render


def home(request):
    return render(request, template_name='pages/home.html')


def about(request):
    return render(request, template_name='pages/about.html')
