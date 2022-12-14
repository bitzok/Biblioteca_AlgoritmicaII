from abc import ABC, abstractmethod

class Atributos():
    def __init__(self):
        self._codigo = None
        self._nombre = None
        self._autor = None
        self._stock = None

class AddProduct(ABC):
    @abstractmethod
    def agregarProducto(self):
        pass

class RemoveProduct(ABC):
    @abstractmethod
    def eliminarProducto(self):
        pass

class ModifyProduct(ABC):
    @abstractmethod
    def modificarProducto(self):
        pass

class ShowStock(ABC):
    @abstractmethod
    def mostrarStock(self):
        pass

class BackToMenu(ABC):
    @abstractmethod
    def volverMenu(self):
        pass

class Menu(ABC):
    @abstractmethod
    def ventanaPrincipal(self):
        pass