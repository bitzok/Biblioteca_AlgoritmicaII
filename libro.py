class Libro():
    def __init__(self, codigo, nombre, autor, stock, edicion):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.stock = stock
        self.edicion = edicion
        self.pedido = False

    def pedirLibro(self):
        self.pedido = True
        pass

    def devolverLibro(self):
        pass

    def reservarLibro(self):
        pass
