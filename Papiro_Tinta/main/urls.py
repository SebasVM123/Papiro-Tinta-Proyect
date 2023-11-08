from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin

from . import views

from . import views2
#from .views import crear_registro

urlpatterns = [
    path('', views.index_view, name='index'),
    path('iniciar-sesion', views.login_view, name='login_url'),
    path('registrarse', views.register_view, name='register_url'),
    path('home/', views.home_view, name='home_url'),
    path('home/mi-perfil', views.client_profile_view, name='client_profile_url')
]
