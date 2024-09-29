from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(req):
    return render(req, 'index.html')

# Formulario de registro
@csrf_exempt
def form_registrar(req):
    return render(req, 'registrar_usuario.html')

# Formulario de login
@csrf_exempt
def form_login(req):
    return render(req, 'login.html')

# Vista del perfil
def perfil(req):
    return render(req, 'perfil.html')

