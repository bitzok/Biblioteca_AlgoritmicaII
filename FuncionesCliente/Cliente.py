from Funciones_DB import *
from FuncionesCliente.Funciones_Cliente import *
from FuncionesCliente.Interfaces_Cliente import *
from abc import ABC, abstractmethod

class Cliente(Atributos):

    db_nombre = "ListaClientes.db"
    """
    def __init__(self):
        self._nombres = None
        self._apellido = None
        self._dni = None
        self._membresia = None"""

    def Llamada(self):
        VentanaPrincipal.ventanaPrincipal(self)

    def consultar(self, query, parameters = ()):
        with sql.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

if __name__ == "__main__":
    app = Cliente()
    app.Llamada()
    
