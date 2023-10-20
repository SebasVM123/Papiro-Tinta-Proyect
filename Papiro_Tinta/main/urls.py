from django.urls import path, include
from django.views.generic import RedirectView

from . import views
#from .views import crear_registro

urlpatterns = [
    path('', views.index_view, name='index'),
    path('iniciar-sesion/', include('django.contrib.auth.urls')),
    path('iniciar-sesion/', views.login_view, name='login_url'),
    path('registrarse/', views.register_view, name='register_url'),
    path('crear-registro/', views.crear_registro, name='crear_registro'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout_url'),
]
