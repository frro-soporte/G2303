"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3
# create a database file
con = sqlite3.connect('soporte_04.db')

#create a cursor 
c = con.cursor()

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """

    c.execute("""CREATE TABLE IF NOT EXISTS persona (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fechaNacimiento DATE NOT NULL,
            dni INTEGER NOT NULL,
            altura INTEGER NOT NULL
            )""")
    con.commit()
    print("Tabla creada con exito")
    # con.close()
# crear_tabla()

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    c.execute("""DROP TABLE IF EXISTS persona""")
    con.commit()
    print("Tabla borrada con exito")
    # con.close()

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
