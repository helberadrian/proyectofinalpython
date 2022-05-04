from unicodedata import name
from django.urls import path
from msn import views

urlpatterns = [
    path("menssage/create/", views.nuevoMensaje, name="nuevoMensaje"),
    path("menssage/", views.mensajes, name="mensajes"),
]