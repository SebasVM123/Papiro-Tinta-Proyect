from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from .views import custom_admin_logout

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
    path('admin/logout/', custom_admin_logout, name='custom_admin_logout'),
    path('admin/', admin.site.urls),
    path('home/perfil', views.client_profile_view, name='client_profile_url')
]
