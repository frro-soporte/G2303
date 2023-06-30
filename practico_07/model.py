"""Base de Datos - ORM"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

from typing import List, Optional

Base = declarative_base()

class Socio(Base):
    __tablename__ = 'socios'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    dni = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))


class DatosSocio():

    def __init__(self):
        """Inicializa la base de datos"""
        self.engine = create_engine('sqlite:///socios.db', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        s = self.session.query(Socio).filter_by(id=id_socio).first()
        return None if s is None else s

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        s = self.session.query(Socio).filter_by(dni=dni_socio).first()
        return None if s is None else s
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        return self.session.query(Socio).all()

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """

        self.session.query(Socio).delete()
        dd = self.session.commit()
        print('DELETE RESULT :: ', dd)
        return True

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        self.session.query(Socio).filter_by(id=id_socio).delete()
        self.session.commit()
        return True
    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        
        self.session.query(Socio).filter_by(id=socio.id).update({
            Socio.nombre: socio.nombre,
            Socio.apellido: socio.apellido,
            Socio.dni: socio.dni
        })
        self.session.commit()
        return socio

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        return self.session.query(Socio).count()
