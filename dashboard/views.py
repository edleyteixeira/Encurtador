from django.shortcuts import render

def register(request):
    return render(request, 'dashboard/register.html')

def login(request):
    return render(request, 'dashboard/login.html')
