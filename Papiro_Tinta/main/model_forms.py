from django import forms
from .models import cliente

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = fields = ['dni', 'nombre', 'apellido', 'fecha_nacimiento', 'direccion', 'ciudad', 'provincia', 'pais',
                           'username', 'password',]
