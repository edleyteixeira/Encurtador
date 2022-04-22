from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.login, name='login'),
    path('addurl/', views.addurl, name='addurl'),
    path('cadastro/', views.cadastro, name='cadastro')
    
]
