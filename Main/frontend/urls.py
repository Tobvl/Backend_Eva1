from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.form_registrar, name='registrar_usuario'),
    path('ingresar/', views.form_login, name='login'),
]
