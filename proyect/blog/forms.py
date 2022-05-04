from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class formUsuario(UserCreationForm):
    email = forms.EmailField()
    descripcion = forms.CharField(max_length=1000)
    foto = forms.CharField(max_length=2000)

    class Meta:
        model = User
        fields = ('username', 'email', 'descripcion', 'foto', 'password1', 'password2')

class formArticulo(forms.Form):
    titulo = forms.CharField(max_length=300)
    subtitulo = forms.CharField(max_length=500)
    contenido = forms.CharField(max_length=200000)
    resumen = forms.CharField(max_length=20000)
    autor = forms.CharField(max_length=200)
    imagen = forms.CharField(max_length=2000)

class formMensaje(forms.Form):
    mensaje = forms.CharField(max_length=2000)
