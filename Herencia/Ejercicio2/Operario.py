from  Empleado import Empleado 

class Operario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)


    def __str__(self):
        return f'Operario: {self._Empleado__nombre}'