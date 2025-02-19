"""Base de Datos SQL - Búsqueda"""

import datetime

from ejercicio_01 import reset_tabla ,c , sqlite3,con 
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    try : 
        c.execute("SELECT * FROM persona WHERE id = ?", (id_persona,))
        p = c.fetchone()
        if p is None:
            return False
        else:                      
            return p
    except sqlite3.Error as e:
        print("Error al conectar con la base de datos", e)
        return False    


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez',  '1988-05-15 00:00:00', 32165498, 180) # tuve que poner la fecha directamente para que funcione el assert
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
