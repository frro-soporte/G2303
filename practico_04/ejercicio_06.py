"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio_01 import borrar_tabla, crear_tabla , c ,  con 

def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    #  FOREIGN KEY(trackartist) REFERENCES artist(artistid)
    c.execute("""CREATE TABLE IF NOT EXISTS personaPeso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idPersona INTEGER NOT NULL,
            fecha DATE NOT NULL,
            peso INTEGER NOT NULL,
            FOREIGN KEY(idPersona) REFERENCES persona(id)
            )""")
    con.commit()
    print("Tabla personaPeso creada con exito")

def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    c.execute("DROP TABLE IF EXISTS personaPeso")
    con.commit()
    print("Tabla personaPeso borrada con exito")

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
