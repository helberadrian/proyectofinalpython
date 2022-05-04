from django.shortcuts import render
from blog.models import Mensaje
from blog.forms import formMensaje
import datetime

# Create your views here.
def mensajes(request):
    mensajes = Mensaje.objects.all()

    if mensajes is not None:
        contexto = {"mensajes": mensajes}
        return render(request, "msn/mensajes.html", contexto)
    else:
        return render(request, "msn/sin_mensajes.html")

def nuevoMensaje(request):
    date = datetime.datetime.now()

    if request.method == "POST":
        miFormulario = formMensaje(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            mensaje = Mensaje(mensaje=info["mensaje"], fecha=date)
            mensaje.save()
            return render(request, "msn/mensajes.html")
    else:
        miFormulario = formMensaje()
    return render(request, "msn/nuevo_mensaje.html", {"miFormulario":miFormulario})