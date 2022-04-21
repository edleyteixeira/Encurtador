from django.db import models
from django.contrib.auth.models import User

class Pixel(models.Model):
    plataform = (
        ("facebook", "Facebook"),
        ("google", "Google"))
    events = (
        ("pageview", "PageView"),
        ("checkout", "InitiateCheckout"))
    evento = models.CharField(max_length=10 , choices=plataform, blank=False, verbose_name='Pixel')
    plataforma = models.CharField(max_length=20 , choices=events, blank=False, verbose_name='Evento')
    pixel_id = models.CharField(max_length=30, verbose_name='id do pixel', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Nome do Pixel', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Encurtadas(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='id')
    urlr = models.URLField(max_length=200, verbose_name='url original')
    slug = models.CharField(unique=True ,max_length=30, verbose_name='Url Atalho')
    plataform = models.ForeignKey(Pixel,on_delete=models.CASCADE, verbose_name='Pixel', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    acessos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.urlr
    
