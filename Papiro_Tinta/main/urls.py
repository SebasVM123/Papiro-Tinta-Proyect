from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login_url'),
]
