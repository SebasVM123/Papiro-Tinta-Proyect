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

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        auth_user = authenticate(request, username=email, password=password)  # Usa username en lugar de email
        
        if auth_user is not None:
            login(request, auth_user)
            return redirect('index')
        else:
            messages.error(request, 'No se pudo iniciar sesión, por favor vuelve a intentar.')  # Cambia a messages.error
            return redirect('login_url')
    else:
        return render(request, 'main/login.html')

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

"""
def crear_registro(request):
    if request.method == 'POST':
        form = MiModeloForm(request.POST)
        if form.is_valid():
            nuevo_cliente = form.save()  # Esto guarda el nuevo cliente en la base de datos
            # Redirige al usuario a la página de éxito o a cualquier otra página que desees.
            return redirect('index')
    else:
        form = MiModeloForm()

    return render(request, 'main/register.html', {'form': form})

"""

"""
def crear_registro(request):
    if request.method == 'POST':
        form = MiModeloForm(request.POST)
        if form.is_valid():
            # Crear una instancia del modelo y completarla con los datos del formulario
            nuevo_cliente = cliente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                contraseña=form.cleaned_data['contraseña'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                direccion=form.cleaned_data['direccion'],
                ciudad=form.cleaned_data['ciudad'],
                provincia=form.cleaned_data['provincia'],
                pais=form.cleaned_data['pais'],
                email=form.cleaned_data['email']
            )
            nuevo_cliente.save()  # Guarda el nuevo cliente en la base de datos

            # Redirige al usuario a la página de éxito o a cualquier otra página que desees.
            return redirect('index')
    else:
        form = MiModeloForm()
        """

"""
def crear_registro(request):
    if request.method == 'POST':
        form = MiModeloForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a la página de éxito o a cualquier otra página que desees.
            return redirect('index')
    else:
        form = MiModeloForm()
        
    return render(request, 'register.html', {'form': form})

"""
















"""
def crear_registro(request):
    if request.method == 'POST':
        form = MiModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        
    else:
        form = MiModeloForm()
        
    return render(request, 'main/templates/register.html', {'form': form})
            
"""