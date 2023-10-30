from django.shortcuts import render, redirect
from .forms import MiModeloForm
from .models import cliente  # Asegúrate de importar el modelo
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
#from django.shortcuts import render, redirect
#from .forms import MiModeloForm

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        auth_user = authenticate(request, username=email, password=password)  # Usa username en lugar de email
        
        if auth_user is not None:
            login(request, auth_user)
            if auth_user.is_superuser:
                return redirect('/admin/')  # Redirige al dashboard del administrador
            else:
                return redirect('home')
        else:
            messages.error(request, 'No se pudo iniciar sesión, por favor vuelve a intentar.')  # Cambia a messages.error
            return redirect('login_url')
    else:
        return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def custom_admin_logout(request):
    logout(request)
    return redirect('index')

def register_view(request):
    return render(request, 'main/register.html')

from django.contrib.auth.models import User
from django.utils import timezone
from .forms import MiModeloForm  # Asegúrate de que tu formulario esté importado correctamente
from django.shortcuts import render, redirect

def crear_registro(request):
    if request.method == 'POST':
        form = MiModeloForm(request.POST)
        if form.is_valid():
            # Crear un nuevo usuario de Django
            username = form.cleaned_data['email']  # Puedes usar el correo electrónico como nombre de usuario, si lo prefieres.
            password = form.cleaned_data['contraseña']  
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()

            # Crear un nuevo cliente
            nuevo_cliente = form.save(commit=False)  # No guardes todavía
            nuevo_cliente.fecha_registro = timezone.now()  # Establece la fecha de registro
            nuevo_cliente.save()  # Ahora guarda la instancia

            return redirect('login_url')
    else:
        form = MiModeloForm()
    return render(request, 'main/register.html', {'form': form})


def client_profile_view(request):
    return render(request, 'main/client_profile.html')