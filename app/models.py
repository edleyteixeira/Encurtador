from django.db import models

class urlEncurtHome(models.Model):
    urlr = models.URLField(max_length=200, verbose_name='url original')
    slug = models.CharField(unique=True ,max_length=7, verbose_name='slug da url')
