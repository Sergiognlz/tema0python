from Empleado import Empleado

class Directivo(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
     
    def __str__(self):
        return f'Directivo: {self._Empleado__nombre}'