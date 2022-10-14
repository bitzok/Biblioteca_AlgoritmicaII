class Institucion(Cliente):
    def __init__(self, tipo, nombreInstitucion):
        super().__init__(tipo)
        self.nombreInstitucion = nombreInstitucion
