# Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca. La clase debe guardar el título del libro, autor, 
# número de ejemplares del libro y número de ejemplares prestados. La clase contendrá los siguientes métodos:
# Constructor con todos los parámetros (se le indica valores para todos los atributos).
# prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo. No se pueden prestar libros si no quedan ejemplares disponibles para prestar. 
# Devuelve true si se ha podido realizar el préstamo y false en caso contrario.
# devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. 
# No se podrán devolver libros que no se hayan prestado. Devuelve true si se ha podido realizar la operación y false en caso contrario.
# Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  libros son iguales si tienen el mismo título y el mismo autor. 
# Los libros se ordenarán de menor a mayor por el nombre del autor.

class Libro:
    def __init__(self,titulo,autor,n_ejemplares,n_prestados):
        self.titulo=titulo
        self.autor=autor
        self.n_ejemplares=n_ejemplares
        self.n_prestados=n_prestados


    def prestamo(self):
        exito=False
        if(self.n_ejemplares>0):
            exito=True
            self.n_prestados+=1
            self.n_ejemplares-=1
        return exito
    
    def devolucion(self):
        exito=False
        if(self.n_prestados>0):
            exito=True
            self.n_prestados-=1
            self.n_ejemplares+=1

        return exito
    
    def __str__(self):
        return "Título: "+self.titulo+" Autor: "+self.autor+" Nº Ejemplares: "+str(self.n_ejemplares)+" Nº Prestados: "+str(self.n_prestados)
    
    def __eq__(self, otroLibro):
        return isinstance(otroLibro,Libro)and(self.titulo==otroLibro.titulo)and(self.autor==otroLibro.autor)
    
    def __lt__(self, otroLibro):
        return isinstance(otroLibro,Libro)and (self.autor<otroLibro.autor)
