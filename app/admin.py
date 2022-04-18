from atexit import register
from django.contrib import admin
from .models import urlEncurtHome

@admin.register(urlEncurtHome)
class UrlHome(admin.ModelAdmin):
    list_display = ('id', 'urlr', 'slug')
