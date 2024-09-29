from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
import os

# API APP views

ARCHIVO_JSON = os.path.join(os.path.dirname(__file__), 'data.json')

def index(req):
    print(ARCHIVO_JSON)
    return HttpResponse("API Index")

# función que devuelve json de los usuarios registrados
@csrf_exempt
def obtener_usuarios(req):
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
    else:
        datos = []
    # retornar los datos en formato json
    return JsonResponse(datos, safe=False)

# función que registra un usuario entregado por POST (en el body)
@csrf_exempt
def registrar_usuario(req):
    if req.method == "POST":
        req_usuario = req.POST.get('username')
        if (existe_usuario(req_usuario)):
            messages.error(req, 'Usuario ya registrado!')
            return redirect('frontend:form_registrar')
        req_email = req.POST.get('email')
        if (existe_correo(req_email)):
            messages.error(req, 'Correo ya registrado!')
            return redirect('frontend:form_registrar')
        req_password = req.POST.get('password')
        nuevo_id = obtener_id()
        nuevo_usuario = {
            'id': nuevo_id,
            'username': req_usuario,
            'email': req_email,
            'password': req_password,
            'seguidores': 0,
            'siguiendo': 0,
            "active": True,
            "login_attempts": 0
        }
        agregar_usuario(nuevo_usuario)
        # Si se registró exitosamente:
        messages.success(req, 'Usuario creado exitosamente!')
        return redirect('frontend:form_login')
        # Si hubo un error:
        # return render(req, 'registro_error.html')
    return redirect('frontend:form_registrar')

# función para autenticar un usuario
@csrf_exempt
def login_usuario(req):
    if req.method == "POST":
        req_email = req.POST.get('email')
        req_password = req.POST.get('password')
        print("llega post con: ", req_email, req_password)
        # Verificar si el correo existe
        existe_correo_bool = existe_correo(req_email)
        if not existe_correo_bool:
            messages.error(req, 'Correo no registrado!')
            print("no existe correo")
            return redirect('frontend:form_login')
        
        intento_login = login(req_email, req_password)
        # intento_login = (usuario, clave_correcta)
        usuario = intento_login[0]
        clave_correcta = intento_login[1]

        if usuario['active'] == False:
            messages.error(req, 'Usuario desactivado por múltiples intentos fallidos!')
            return redirect('frontend:form_login')

        if usuario is None or clave_correcta == False:
            messages.error(req, 'Usuario o contraseña incorrectos!')
            return redirect('frontend:form_login')

        if intento_login[1] == "Desactivado":
            messages.error(req, 'Se ha bloqueado tu cuenta por múltiples intentos fallidos!')
            return redirect('frontend:form_login')
        
        
        # Si se logueó exitosamente almacenar datos en la request
        req.session['username'] = usuario['username']
        req.session['email'] = usuario['email']
        req.session['seguidores'] = usuario['seguidores']
        req.session['siguiendo'] = usuario['siguiendo']
        
        return redirect('frontend:perfil')
    
    return redirect('frontend:form_login')

# función para cerrar sesión
@csrf_exempt
def logout_usuario(req):
    req.session.flush()
    messages.success(req, 'Sesión cerrada exitosamente!')
    return redirect('frontend:form_login')

def agregar_usuario(usuario):
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
    else:
        datos = {
            'usuarios': []
        }
    # agregar el usuario
    datos['usuarios'].append(usuario)
    # abrir el archivo como escritura
    with open(ARCHIVO_JSON, 'w') as f:
        # guardar los datos en el archivo como json
        json.dump(datos, f)

def existe_correo(correo):
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
            # recorrer los datos
            usuarios = datos['usuarios']
            for user in usuarios:
                if user['email'] == correo:
                    return True
    # retornar False
    return False

def existe_usuario(usuario):
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
            # recorrer los datos
            usuarios = datos['usuarios']
            for user in usuarios:
                if user['username'] == usuario:
                    return True
    # retornar False
    return False

def obtener_id():
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
            # recorrer los datos
            usuarios = datos['usuarios']
            if len(usuarios) == 0:
                return 1
            else:
                return usuarios[-1]['id'] + 1
    # retornar 1
    return 1

# función para autenticar un usuario
# retorna el usuario y un booleano que indica si la clave es correcta
def login(correo, contrasena):
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
            # recorrer los datos
            usuarios = datos['usuarios']
            for user in usuarios:
                if user['email'] == correo and user['password'] == contrasena:
                    # Login en la session y retornar el usuario
                    return user, True
                if user['email'] == correo and user['password'] != contrasena:
                    intentos = agregar_intento(correo)
                    if intentos >= 3:
                        return user, "Desactivado"
                    return user, False
    # retornar None
    return None, False

def agregar_intento(correo):
    intentos = 0
    # si existe el archivo
    if os.path.exists(ARCHIVO_JSON):
        # abrir el archivo como lectura
        with open(ARCHIVO_JSON, 'r') as f:
            # cargar los datos del archivo como json
            datos = json.load(f)
    else:
        datos = {
            'usuarios': []
        }
    # recorrer los datos
    usuarios = datos['usuarios']
    for user in usuarios:
        if user['email'] == correo and user['active'] == True:
            user['login_attempts'] += 1
            if user['login_attempts'] >= 3:
                user['active'] = False
                intentos = user['login_attempts']
    # abrir el archivo como escritura
    with open(ARCHIVO_JSON, 'w') as f:
        # guardar los datos en el archivo como json
        json.dump(datos, f)
    return intentos