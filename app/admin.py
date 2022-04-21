from django.contrib import admin
from .models import Pixel, Encurtadas

@admin.register(Encurtadas)
class EncurtadasAdmin(admin.ModelAdmin):
    list_display = ('id', 'urlr', 'slug', 'plataform', 'acessos', 'user')
    list_display_links = ('id',  'slug')
    
    
@admin.register(Pixel)
class PixelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pixel_id')
    list_display_links = ('id', 'name', 'pixel_id')
    

