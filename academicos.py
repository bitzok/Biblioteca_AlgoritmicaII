class Academicos(Libro):
    def __init__(self, codigo, nombre, autor, stock, edicion, rama, editorial):
        super().__init__(codigo, nombre, autor, stock, edicion)
        self.rama = rama
        self.editorial = editorial
