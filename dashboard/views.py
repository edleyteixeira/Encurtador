from multiprocessing import context
from django.shortcuts import render
from allauth.account.forms import (
    LoginForm,
    SignupForm,
)

from app.models import *

def home(request):
    return render(request, 'dashboard/home.html')

def login(request):
    context= {
        'form': LoginForm()
    }
    return render(request, 'dashboard/login.html', context)


