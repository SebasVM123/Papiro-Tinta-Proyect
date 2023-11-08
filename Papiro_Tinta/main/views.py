from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from .model_forms import *


def index_view(request):
    return render(request, 'main/index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)

        user = authenticate(request, username=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home_url')

        return redirect('login_url')
    else:
        return render(request, 'main/login.html')


def register_view(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.fecha_registro = timezone.now()
            new_client.save()

            return redirect('login_url')
        else:
            print(form.errors)
    else:
        return render(request, 'main/register.html')


def home_view(request):
    return render(request, 'main/home.html')


def client_profile_view(request):
    return render(request, 'main/client_profile.html')