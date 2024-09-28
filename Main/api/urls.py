from django.urls import path
from . import views

# urls de la app api
urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.obtener_usuarios, name='obtener_usuarios'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]