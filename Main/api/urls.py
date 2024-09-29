from django.urls import path
from . import views

# urls de la app api
app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.obtener_usuarios, name='obtener_usuarios'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('usuarios/logout/', views.logout_usuario, name='logout_usuario'),
]