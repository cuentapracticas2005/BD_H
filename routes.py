
from flask import Flask, render_template, request, url_for, session
from funciones import * # Importando mis funciones personalizadas

# Declarando nombre de la aplicación e inicializando Flask
app = Flask(__name__)
application = app  # Alias de app, a veces se usa en servidores como Gunicorn

app.secret_key = '84d8ewd4e8de9f59ef9f5f1v5f1f5vd35fv1df64gf4g5df4g5df64g88t8g4g4g455g5g5gg4g000g4bg4g48g6dfgb0gf5b4'


#-------------------------- MANEJO DE ERRORES ------------------------------

#Redireccionamineto cuando la pagina no existe
@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('src/templates/public/pages/admin/interac_admin.html')