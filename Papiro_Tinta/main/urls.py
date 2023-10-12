from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('iniciar-sesion/', views.login_view, name='login_url'),
    path('registrarse/', views.register_view, name='register_url')
]
