from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            messages.success(request, ('No se pudo iniciar sesion, por favor vuelve a intentar'))
            return redirect('login_url')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'main/login.html')

def register_view(request):
    return render(request, 'main/register.html')