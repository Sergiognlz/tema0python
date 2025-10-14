# A continuación, define dos clases, Gato y Perro que heredan de Animal. En el caso de Gato, además del constructor, 
# definirá los siguientes métodos:
# habla: Devolverá ‘Miau’.
#__str__: Primero escribirá “Soy un gato” y a continuación la misma cadena que el padre.

from Animal import Animal

class Gato(Animal): 

    def __init__(self,nombre,nPatas):
        super().__init__(nombre,nPatas)

    def habla(self):
        return 'Miau'

    def __str__(self):
        return f'Soy un gato. {super().__str__()}'