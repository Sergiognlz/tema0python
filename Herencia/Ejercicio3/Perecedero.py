from Producto   import Producto

class Perecedero(Producto):
    def __init__(self, nombre, precio, dias_a_caducar ):
        super().__init__(nombre, precio)
        self.dias_a_caducar = dias_a_caducar

    def __str__(self):
        return f"{super().__str__()}, Días a caducar: {self.dias_a_caducar}"
    
    def Calcular(self,cantidad):
        precioFinal = super().Calcular(cantidad)
        
        if self.dias_a_caducar == 1:
            precioFinal *= 0.25
        elif self.dias_a_caducar == 2:  
            precioFinal *= 0.3
        elif self.dias_a_caducar == 3:
            precioFinal *= 0.5


        return precioFinal