from Producto   import Producto

class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo ):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Material: {self.tipo}"
    
    def Calcular(self,cantidad):
        return super().Calcular(cantidad)
    
    