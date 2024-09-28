from django.shortcuts import render, HttpResponse

# Create your views here.

def index(req):
    return HttpResponse("Frontend Index")

# Formulario de registro
def form_registrar(req):
    return render(req, 'registrar_usuario.html')

# Formulario de login
def form_login(req):
    return render(req, 'login.html')