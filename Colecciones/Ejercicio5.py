#Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10. 
# Luego pedirá un valor N y mostrará cuántas veces aparece N. 


#importamos la clase random
import random
#creamos la una lista 
lista=[]
#usamos un for para recorrer 100 posiciones(de 0 a 99)
for i in range(100):
    #rellenamos la lista usando lista.append con números random entre 1 y 10(ambos inclusive)
    lista.append(random.randint(1,10))

#pedimos un número al usuario y lo guardamos en una variable num
num=int(input("Introduce un número para buscar cuantas veces aparece"))
#declaramos una variable contador donde contaremos cuantas veces aparece un número en la lista
cont=0
#for para recorrer la lista
for n in lista:
    #si el número en el que nos encontramos es igual al que buscamos...
    if(n==num):
        #contar+1
        cont+=1

#imprimimos contador
print(cont)