from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('index.html', RedirectView.as_view(url='/index', permanent=True)),
    path('login/', views.login, name='login'),
]
