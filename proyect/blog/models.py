from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=1000)
    foto = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}, Email: {self.email}, Contraseña: {self.password}, Descripcion: {self.descripcion}, Foto: {self.foto}"

class Articulo(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=500)
    contenido = models.CharField(max_length=200000)
    resumen = models.CharField(max_length=20000)
    autor = models.CharField(max_length=200)
    imagen = models.CharField(max_length=2000)
    fecha = models.DateField()

    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Subtitulo: {self.subtitulo}, Contenido: {self.contenido}, Resumen: {self.resumen}, Autor: {self.autor}, Imagen: {self.imagen}, Fecha: {self.fecha}"

class Mensaje(models.Model):
    mensaje = models.CharField(max_length=5000)
    fecha = models.DateField()

    def __str__(self) -> str:
        return f"Mensaje: {self.mensaje}, Fecha: {self.fecha}"

