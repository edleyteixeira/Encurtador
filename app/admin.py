from atexit import register
from django.contrib import admin
from .models import Pixel, Encurtadas

@admin.register(Encurtadas)
class EncurtadasAdmin(admin.ModelAdmin):
    list_display = ('id', 'urlr', 'slug')
    
@admin.register(Pixel)
class PixelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pixel_id')
    
    
