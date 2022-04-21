from django.shortcuts import render
from app.models import Encurtadas


from .forms import Encurtar
import random, string



def home(request):
    if request.method == 'POST':
        form = Encurtar(request.POST)
        if form.is_valid():
            url_encurtada = form.cleaned_data['url_original']
            slug = random.choice(string.ascii_letters)+ random.choice(string.ascii_letters)+ random.choice(string.ascii_letters)+ random.choice(string.ascii_letters)+ random.choice(string.ascii_letters)+ random.choice(string.ascii_letters)+ random.choice(string.ascii_letters)
            encurtada = Encurtadas(urlr=url_encurtada, slug=slug)
            encurtada.save()
            context = {
            'slug' : slug,
            'form' : Encurtar()
            }
            return render(request, 'templates/app/home.html', context)
    else:
        context = {
    
            'form' : Encurtar()
        }
        return render(request, 'app/home.html', context)
    

def faq(request):
    return render(request, 'app/faq.html')

def contato(request):
    return render(request, 'app/contato.html')
    
def url(request, url):
    
    acessos = Encurtadas.objects.filter(slug=url).get()
    acessos.acessos = acessos.acessos + 1
    acessos.save()

    context = {
       'redirect': acessos,
        
    }
    return render(request, 'app/redirect.html', context)
    