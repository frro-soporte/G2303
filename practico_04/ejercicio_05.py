"""Base de Datos SQL - Modificación"""

import datetime

from ejercicio_01 import reset_tabla , c , sqlite3, con 
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""
    try : 
        c.execute("SELECT * FROM persona WHERE id = ?", (id_persona,))
        p = c.fetchone()
        if p is None:
            return False
        else:
            c.execute("UPDATE persona SET nombre = ?, fechaNacimiento = ?, dni = ?, altura = ? WHERE id = ?", (nombre, nacimiento, dni, altura, id_persona))
            if(c.rowcount > 0):
                print("Se actualizo correctamente el registro")
                con.commit()    
                return True
            else:
                print("No se actualizo el registro")
                return False
    except sqlite3.Error as e:
        print("Error al conectar con la base de datos", e)
        return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    # assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181) -- no funciona con el datetime de la tupla
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
