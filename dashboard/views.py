
from django.shortcuts import render
from dashboard.forms import userID
from app.models import Encurtadas

from app.models import *

def home(request):
    return render(request, 'dashboard/home.html')

def login(request):
    context= {
        #'form': 
    }
    return render(request, 'dashboard/login.html', context)

def cadastro(request):
    context = {
        #'form' : 
    }
    return render(request, 'dashboard/register.html', context)


def addurl(request):
    if request.method == "POST":
        form = userID(request.POST)
        if form.is_valid():
           links = Encurtadas.objects.get(user_id=form.cleaned_data['id_user'])
           
        
    context = {
        'form': userID()
    }
    return render(request, 'dashboard/addurl.html', context)

