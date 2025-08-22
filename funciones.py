from flask import session
from conexion import *

#Se crea una funcion y dentro de ella una data(un diccionario)
#con valores del usuario ya logueado
def dataLoginSesion():
    inforLogin = {
        "idLogin"       :session['id_user'],
        "userLogin"     :session['nombre'],
        "passwordLogin" :session['password']
    }
    return inforLogin

def dataPerfilUser():
    conexion_MySQL = connectionDB() #Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQL.cursor(dictionary=True) #Creo un cursor para poder ejecutar las consultas SQL
    idUser = session['id_user'] #Creo una variable para almacenar el id del usuario logueado

    querySQL = "SELECT * FROM login_python WHERE id=%s"
    mycursor.execute(querySQL, (idUser,))
    datosUsuario = mycursor.fetchone()
    mycursor.close() #Cerrando conexion SQL
    conexion_MySQL.close() #Cerrando conexion MySQL
    return datosUsuario #Retornando los datos del usuario