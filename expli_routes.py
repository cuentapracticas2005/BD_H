from flask import Flask, render_template, redirect, url_for, session
from funciones import *  # Importando mis funciones personalizadas (listaPaises, dataLoginSesion, dataPerfilUsuario, etc.)

# Declarando nombre de la aplicación e inicializando Flask
app = Flask(__name__)
application = app  # Alias de app, a veces se usa en servidores como Gunicorn

# Clave secreta necesaria para manejar sesiones de usuario en Flask
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'


# -------------------- MANEJADOR DE ERRORES --------------------

# Redireccionando cuando la página no existe (Error 404)
@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:  # Si el usuario está logueado
        return redirect(url_for('inicio'))  # Lo manda al inicio/dashboard
    else:  # Si no está logueado
        # Muestra la página de login y pasa la lista de países
        return render_template('public/modulo_login/index.html', dataPaises=listaPaises())
    

# -------------------- RUTA PRINCIPAL (HOME) --------------------

@app.route('/')
def inicio():
    if 'conectado' in session:  # Si el usuario está logueado
        # Renderiza el home del dashboard con datos de sesión
        return render_template('public/dashboard/home.html', dataLogin=dataLoginSesion())
    else:  # Si no está logueado
        # Renderiza el login con la lista de países
        return render_template('public/modulo_login/index.html', dataPaises=listaPaises())
    

# -------------------- LOGIN --------------------

@app.route('/login')
def login():
    if 'conectado' in session:  # Si ya está logueado
        # Lo manda directo al home del dashboard
        return render_template('public/dashboard/home.html', dataLogin=dataLoginSesion())
    else:
        # Caso contrario muestra el login
        return render_template('public/modulo_login/index.html', dataPaises=listaPaises())


# -------------------- EDITAR PERFIL --------------------

@app.route('/edit-profile', methods=['GET', 'POST'])
def editProfile():
    if 'conectado' in session:  # Solo usuarios logueados pueden entrar
        # Renderiza la vista del perfil con:
        # - Datos del usuario
        # - Datos de la sesión
        # - Lista de países
        return render_template(
            'public/dashboard/pages/Profile.html',
            dataUser=dataPerfilUsuario(),
            dataLogin=dataLoginSesion(),
            dataPaises=listaPaises()
        )
    # Si no está logueado, lo redirige al inicio/login
    return redirect(url_for('inicio'))


# -------------------- CERRAR SESIÓN --------------------

@app.route('/logout')
def logout():
    msgClose = ''
    # Eliminar datos de la sesión → esto cierra la sesión del usuario
    session.pop('conectado', None)  # Borra la variable "conectado"
    session.pop('id', None)         # Borra el id del usuario
    session.pop('email', None)      # Borra el correo electrónico

    # Mensaje de confirmación de cierre de sesión
    msgClose = "La sesión fue cerrada correctamente"

    # Vuelve al login y muestra un mensaje de alerta (msjAlert)
    # typeAlert=1 → puede ser tipo de notificación (éxito, info, etc.)
    return render_template('public/modulo_login/index.html', msjAlert=msgClose, typeAlert=1)
