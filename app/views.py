from django.shortcuts import render
from app.models import urlEncurtHome

def home(request):
    return render(request, 'app/home.html')

def faq(request):
    return render(request, 'app/faq.html')

def contato(request):
    return render(request, 'app/contato.html')
    
def url(request, url):
    redirect = urlEncurtHome.objects.filter(slug=url)
    
    context = {
        'redirect': redirect
    }
    return render(request, 'app/redirect.html', context)
    