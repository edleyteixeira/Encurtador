from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def faq(request):
    return render(request, 'app/faq.html')

def contato(request):
    return render(request, 'app/contato.html')
    
    