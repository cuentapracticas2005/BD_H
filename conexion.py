import mysql.connector #Se importa libreria mysql.connector para conectar python con mysql

def connectionDB():
    mydb = mysql.connector.connect( #Se crea la variable mydb para conectar a la base de datos
        host="localhost",
        user="root",
        password="",
        database="db_h"
    )
    return mydb