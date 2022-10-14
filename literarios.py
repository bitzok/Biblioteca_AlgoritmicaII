class Literarios(Libro):
    def __init__(self, codigo, nombre, autor, stock, edicion, genero, editorial):
        super().__init__(codigo, nombre, autor, stock, edicion)
        self.genero = genero
        self.editorial = editorial
