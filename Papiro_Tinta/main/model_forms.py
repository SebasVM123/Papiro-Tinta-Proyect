from django import forms
from .models import cliente

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['dni', 'nombre', 'apellido', 'fecha_nacimiento', 'email', 'contraseña', 'direccion', 'ciudad',
                  'provincia', 'pais',]