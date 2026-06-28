from modelos.persona import Persona

class Usuario(Persona):

    def __init__(self,
                 identificacion,
                 nombre,
                 correo,
                 telefono):

        super().__init__(identificacion, nombre)

        self.correo = correo
        self.telefono = telefono