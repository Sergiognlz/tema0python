#Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

#importamos la clase random
import random
#creamos la una lista 
lista=[]
#usamos un for para recorrer 10 posiciones(de 0 a 9)
for i in range(10):
    #rellenamos la lista usando lista.append con números random entre 1 y 100(ambos inclusive)
    lista.append(random.randint(1,100))

#imprimimos lista
print(lista)