from Funciones_DB import *
from Funciones.Funciones_Admin import *
from abc import ABC, abstractmethod

class I_Clases(ABC):
    @abstractmethod
    def Llamada(self):
        pass

    @abstractmethod
    def consultar(self, consulta, parameters):
        pass
        
class Admin(I_Clases):

    db_nombre = "StockLibros.db"

    def __init__(self):
        self.codigo = None
        self.nombre = None
        self.autor = None
        self.stock = None

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
    app = Admin()
    app.Llamada()
    