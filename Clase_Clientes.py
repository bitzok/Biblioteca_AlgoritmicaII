from Funciones_DB import *
from FuncionesCliente.Funciones_Cliente import *
from FuncionesCliente.Interfaces_Cliente import *
from abc import ABC, abstractmethod

class I_Clases(ABC):
    @abstractmethod
    def Llamada(self):
        pass

    @abstractmethod
    def consultar(self, consulta, parameters):
        pass
        
class Cliente(I_Clases, Atributos):

    def __init__(self):
        super().__init__()

    db_nombre = "ListaClientes.db"

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
    