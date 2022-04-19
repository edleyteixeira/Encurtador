from django.db import models
from django.contrib.auth.models import User

class Pixel(models.Model):
    plataform = (
        ("facebook", "Facebook"),
        ("google", "Google"))
    plataforma = models.CharField(max_length=10 , choices=plataform, blank=False, verbose_name='PIXEL')
    pixel_id = models.CharField(max_length=30, verbose_name='id do pixel', blank=False)
    name = models.CharField(max_length=100, verbose_name='Nome do Pixel', blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    



    
class Encurtadas(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='id')
    urlr = models.URLField(max_length=200, verbose_name='url original')
    slug = models.CharField(unique=True ,max_length=7, verbose_name='slug da url')
    plataform = models.ForeignKey(Pixel,on_delete=models.CASCADE, verbose_name='Pixel')
    name_p = models.CharField(max_length=30, verbose_name='url personalizada')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.urlr
    