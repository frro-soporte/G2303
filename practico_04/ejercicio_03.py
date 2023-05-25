"""Base de Datos SQL - Baja"""

import datetime

from ejercicio_01 import reset_tabla ,c , sqlite3,con 
from ejercicio_02 import agregar_persona

def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    try : 
        c.execute("SELECT * FROM persona WHERE id = ?", (id_persona,))
        p = c.fetchone()
        if p is None:
            return False
        else:
            c.execute("DELETE FROM persona WHERE id = ?", (id_persona,))
            con.commit()               
            return True
    except sqlite3.Error as e:
        print("Error al conectar con la base de datos", e)
        return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
