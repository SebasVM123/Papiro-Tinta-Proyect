from django import forms
from .models import cliente

class MiModeloForm(forms.ModelForm):
    class Meta:
        model=cliente
        fields=['nombre', 'apellido', 'contraseña', 'fecha_nacimiento', 'direccion', 'ciudad', 'provincia', 'pais', 'email']
        

  