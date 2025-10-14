# Define una clase llamada Animal que tiene como atributos nombre y número de patas. Además del constructor, define los siguientes métodos:
# habla: En la clase Animal devolverá una cadena vacía, ‘’.
# __str__: Devolverá una cadena de la siguiente forma: “Me llamo nombre, tengo x patas y sueno así: sonido”. 
# Habrá que sustituir lo que está en azul por el nombre y el número de patas del animal. En el caso de sonido hay que llamar a la función habla.

class Animal:

    def __init__(self,nombre,nPatas):
        self.nombre=nombre
        self.nPatas=nPatas

    def getNombre(self):
        return self.nombre
    
    def getNPatas(self):
        return self.nPatas

    def __str__(self):
        return f'Me llamo {self.nombre}, tengo {self.nPatas} patas y sueno así: {self.habla()}'

    def habla(self):
        return ''