from Operario import Operario


class Oficial(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return f'Oficial: {self._Empleado__nombre}'

