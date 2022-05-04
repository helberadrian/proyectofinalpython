from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blog.forms import formUsuario, formArticulo
from blog.models import Usuario, Articulo, Mensaje
from django.views.generic.list import ListView
from django.contrib.auth.models import User
import datetime

#Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "blog/index.html")

def todosArticulos(request):
    articulos = Articulo.objects.all()

    if not articulos:
        return render(request, "blog/no_disponible.html")
    else:
        contexto = {"articulos": articulos}
        return render(request, "blog/pages.html", contexto)
    
def about(request):
    return render(request, "blog/about.html")

def noDisponible(request):
    return render(request, "blog/no_disponible.html")

def detalleArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    contexto= {"articulo":articulo}
    return render(request, "blog/articulos_detalle.html", contexto)

def success(request):
    return render(request, "blog/success.html")

#View del Login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "blog/pages.html")
            else:
                return render(request, "blog/login.html", {"mensaje": "Error, los datos ingresados son incorrectos..."})
        
        else:
            return render(request, "blog/pages.html", {"mensaje": "Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "blog/login.html", {"form":form})

def registro(request):
    if request.method == "POST":
        form = formUsuario(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "blog/success.html")
    else:
        form = formUsuario()
        return render(request, "blog/registro.html", {"form":form})

@login_required
def admin(request):
    return render(request, "blog/admin.html")

def crearArticulo(request):
    date = datetime.datetime.now()

    if request.method == "POST":
        miFormulario = formArticulo(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            article = Articulo(titulo=info["titulo"], contenido=info["contenido"], resumen=info["resumen"], imagen=info["imagen"], fecha=date)
            article.save()
            return render(request, "blog/success.html")
    else:
        miFormulario = formArticulo()
    return render(request, "blog/articulo_nuevo.html", {"miFormulario":miFormulario})

def editarArticulo(request, id):
      articulo = Articulo.objects.get(id=id)
      if request.method == 'POST':
            miFormulario = formArticulo(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  articulo.titulo = informacion['titulo']
                  articulo.subtitulo = informacion['subtitulo']
                  articulo.contenido = informacion['contenido']
                  articulo.resumen = informacion['resumen']
                  articulo.autor = informacion['autor']
                  articulo.imagen = informacion['imagen']
                  articulo.save()
                  return render(request, "blog/success.html")
      else: 
            miFormulario= formArticulo(initial={'titulo': articulo.titulo, 'subtitulo': articulo.subtitulo, 'contenido':articulo.contenido , 
            'resumen':articulo.resumen, 'autor': articulo.autor, 'imagen':articulo.imagen})
      return render(request, "blog/articulos_update.html", {"miFormulario":miFormulario})

def eliminarArticulo(request, id):
      articulo = Articulo.objects.get(id=id)
      articulo.delete()

      articulos = Articulo.objects.all()
      contexto= {"articulos":articulos}
      return render(request, "blog/success.html", contexto)

def perfilUsuario(request):
    usuario = request.user
    
    contexto = {"usuario": usuario.username, "email": usuario.email}
    return render(request, "blog/usuario_profile.html", contexto)

def editarUsuario(request):
      usuario = request.user
      if request.method == 'POST':
            miFormulario = formUsuario(request.POST)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario.username = informacion['usuario']
                  usuario.email = informacion['email']
                  usuario.password = informacion['password']
                  usuario.save()
                  return render(request, "blog/success.html")
      else: 
            miFormulario= formUsuario(initial={'usuario': usuario.username, 'email':usuario.email , 
            'password':usuario.password})
      return render(request, "blog/usuario_update.html", {"miFormulario":miFormulario})

# class perfilUsuario(DetailView):
#     model = Usuario
#     template_name = "blog/usuario_profile.html"