from django.urls import path
from . import views

# urls de la app frontend
app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.form_registrar, name='form_registrar'),
    path('ingresar/', views.form_login, name='form_login'),
    path('perfil/', views.perfil, name='perfil'),
]
