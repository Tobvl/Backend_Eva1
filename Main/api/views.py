from django.shortcuts import render
from django.http import JsonResponse
import json
import os

# API APP views

ARCHIVO_JSON = os.path.join(os.path.dirname(__file__), 'data.json')

def index(req):
    return render(req, 'index.html')

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

def registrar_usuario(req):
    if req.method == "POST":
        ...
        # return render(req, 'registro_exitoso.html')
    #return render(req, 'registrar_usuario.html')

