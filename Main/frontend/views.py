from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

def index(req):
    return render(req, 'index.html')

# Formulario de registro
@csrf_exempt # Desactiva la protección CSRF
def form_registrar(req):
    return render(req, 'registrar_usuario.html')

# Formulario de login
@csrf_exempt # Desactiva la protección CSRF
def form_login(req):
    return render(req, 'login.html')

# Vista del perfil
def perfil(req):

    usuario = req.session.get('username')
    correo = req.session.get('email')
    seguidores = req.session.get('seguidores')
    siguiendo = req.session.get('siguiendo')

    if (usuario == None or
        correo == None or
        seguidores == None or
        siguiendo == None):
        messages.error(req, 'Debes iniciar sesión para ver tu perfil!')
        return redirect('frontend:form_login')
    
    return render(req, 'perfil.html', {
        'usuario': usuario,
        'correo': correo,
        'seguidores': seguidores,
        'siguiendo': siguiendo
    })

