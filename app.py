#IMPORTACION DE PAQUETES A UTILIZAR
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
from datetime import datetime

from conexion import * #Se importa la funcion connectionDB del archivo conexion.py
from funciones import * #Se importan las funciones del archivo funciones.py
from routes import * #Se importan las rutas del archivo routes.py

import re
from werkzeug.security import generate_password_hash, check_password_hash #Paquete para poder encriptar contraseñas

