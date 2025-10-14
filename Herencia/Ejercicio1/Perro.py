# En el caso de Perro, además del constructor, definirá los siguientes métodos:
# habla: Devolverá “Guau”.
# __str__: Primero escribirá “Soy un perro” y a continuación la misma cadena que el padre.

from Animal import Animal

class Perro(Animal): 

    def __init__(self,nombre,nPatas):
        super().__init__(nombre,nPatas)

    def habla(self):
        return 'Guau'

    def __str__(self):
        return f'Soy un perro. {super().__str__()}'