from django.urls import path
from blog import views

#login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("success/", views.success, name="success"),
    #CRUD Articulos
    path("page/", views.todosArticulos, name="todos"),
    path("create/", views.crearArticulo, name="nuevo"),
    path("page/<id>/", views.detalleArticulo, name="detalle"),
    path("update/<id>/", views.editarArticulo, name="editar"),
    path("delete/<id>/", views.eliminarArticulo, name="eliminar"),
    path("notAvailable/", views.noDisponible, name="noDisponible"),
    #Login y Usuario
    path("accounts/login/", views.login_request, name="login"),
    path("accounts/profile/", views.perfilUsuario, name="perfil"),
    path("accounts/update/", views.editarUsuario, name="editarUsuario"),
    path("accounts/signup/", views.registro, name="registro"),
    path("accounts/logout/", LogoutView.as_view(template_name= "blog/logout.html"), name="logout"),
    path("blog/admin/", views.admin, name="admin"),
]