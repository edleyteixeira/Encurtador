from multiprocessing import context
from django.shortcuts import render
from allauth.account.forms import (
    AddEmailForm,
    ChangePasswordForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    SetPasswordForm,
    SignupForm,
    UserTokenForm,
)

def home(request):
    return render(request, 'dashboard/home.html')

def login(request):
    context= {
        'form': LoginForm()
    }
    return render(request, 'dashboard/login.html', context)


