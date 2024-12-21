from django import forms
from .models import *
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class FormParticipante(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'
        widgets = {
            'institucion': forms.Select(attrs={'class': 'form-control'}),  # Campo para instituciones
            'nro_personas': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 xxxx xxxx',
                'maxlength': '15',
                'title': 'Formato: +56 9 xxxx xxxx'
            }),
            'fecha_inscripcion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_inscripcion': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("El correo electrónico no es válido.")
        return email

    def clean_nro_personas(self):
        nro_personas = self.cleaned_data.get('nro_personas')
        if nro_personas < 1 or nro_personas > 30:
            raise forms.ValidationError("El número de personas debe estar entre 1 y 30.")
        return nro_personas

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\+56 9 \d{4} \d{4}$', telefono):
            raise forms.ValidationError("El número debe tener el formato '+56 9 xxxx xxxx'.")
        return telefono

class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Institución'}),

        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) > 80:
            raise forms.ValidationError("El nombre de la institución no puede superar los 80 caracteres.")
        return nombre
    
