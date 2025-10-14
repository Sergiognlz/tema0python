
class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"   
    
    def Calcular(self,cantidad):
        return self.precio * cantidad  
    
    def __Lt__(self,otro):
        return self.precio < otro.precio



     
    