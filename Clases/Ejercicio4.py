# Crea una clase llamada Articulo con los siguientes atributos: nombre, precio (sin IVA), iva (siempre será 21) y cuantosQuedan (representa cuántos quedan en el almacén).
# Añade los siguientes métodos:
# Constructor con 3 parámetros que asigne valores a nombre, precio y cuantosQuedan. El IVA siempre lo pondrá a 21.
# Método getPVP que devuelva el precio de venta al público (PVP) con iva incluido. 
# Método getPVPDescuento que devuelva el PVP con un descuento pasado como argumento. 
# Método vender que actualiza los atributos del objeto tras vender una cantidad ‘x’ (si es posible). Devolverá true si ha sido posible (false en caso contrario). 
# La cantidad a vender se pasará como argumento al método.
# Método almacenar que actualiza los atributos del objeto tras almacenar una cantidad ‘x’. La cantidad a almacenar se pasará como argumento.
# Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  artículos son iguales si tienen el mismo nombre. 
# Los artículos se ordenarán de menor a mayor por el nombre.


iva=0.21

class Articulo:
    def __init__(self,nombre,precio, cuantos_quedan):
        self.nombre=nombre
        self.precio=precio
        self.cuantos_quedan=cuantos_quedan

    def get_PVP(self):
        return self.precio+(self.precio*iva)

    def get_PVP_descuento(self,descuento):
        return  (self.precio+(self.precio*iva))-((self.precio+(self.precio*iva))*descuento)/100
    
    def vender(self,cantidad):
        exito=False

        if(self.cuantos_quedan>=cantidad):
            exito=True
            self.cuantos_quedan-=cantidad

        return exito
    
    def almacenar(self,cantidad):
        self.cuantos_quedan+=cantidad

    def __str__(self):
        return "Artículo: "+self.nombre+" Precio: "+str(self.precio)+" Stock: "+str(self.cuantos_quedan)

    def __eq__(self, otroArticulo):
        return isinstance(otroArticulo,Articulo) and self.nombre==otroArticulo.nombre
    
    def __lt__(self,otroArticulo):
        return isinstance(otroArticulo,Articulo) and self.nombre<otroArticulo.nombre

if __name__=="__main__":
    articulo1=Articulo("Escobilla del wáter",3.0,25)

    
    print(articulo1.get_PVP_descuento(10))
