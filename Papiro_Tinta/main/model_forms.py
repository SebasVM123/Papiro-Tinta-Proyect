from django import forms
from .models import cliente

class clienteModel(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'