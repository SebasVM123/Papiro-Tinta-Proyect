#from django.shortcuts import render, redirect
#from .forms import MiModeloForm
from django.shortcuts import render, redirect
from .forms import MiModeloForm
from .models import cliente  # Asegúrate de importar el modelo
from django.utils import timezone



# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')

def login_view(request):
    return render(request, 'main/login.html')

def register_view(request):
    return render(request, 'main/register.html')

def crear_registro(request):
    if request.method == 'POST':
        form = MiModeloForm(request.POST)
        if form.is_valid():
            nuevo_cliente = form.save(commit=False)  # No guardes todavía
            nuevo_cliente.fecha_registro = timezone.now()  # Establece la fecha de registro
            nuevo_cliente.save()  # Ahora guarda la instancia
            return redirect('index')
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