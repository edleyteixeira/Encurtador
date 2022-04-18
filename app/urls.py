from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:url>', views.url, name='url'),
    path('faq/', views.faq, name='faq'),
    path('contato/', views.contato, name='contato')    
    
]
