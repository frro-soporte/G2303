"""Base de Datos SQL - Alta"""

import datetime
from ejercicio_01 import reset_tabla
from ejercicio_01 import c , sqlite3,con 

def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    try : 
        c.execute("INSERT INTO persona VALUES (NULL, ?, ?, ?, ?)", (nombre, nacimiento, dni, altura))
        print('simple last id :: ', c.lastrowid)
        con.commit()   
        # last_id = c.execute('SELECT last_insert_rowid()' )
        # p = last_id.fetchall()
        # return p[0][0]
        return c.lastrowid
    except sqlite3.Error as e:
        print("Error al conectar con la base de datos", e)
    # finally: 
        # con.close()
# def insert_person(nombre, fechaNacimiento, dni, altura) -> int: 


        
# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
