from Funciones_DB import *
from Funciones.Funciones_Admin import *
from Funciones.Interfaces_Admin import *
from abc import ABC, abstractmethod

class Admin():
    def __init__(self):
        super().__init__()
    
    db_nombre = "StockLibros.db"

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
    
