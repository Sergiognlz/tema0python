#Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.


#creamos la una lista 
lista=[]
#usamos un for para recorrer 10 posiciones(de 0 a 9)
for i in range(10):
    #pedimos al usuario un número y lo guardamos en la variable num
    num=int(input("Introduce un número "+str((i+1))))
    #rellenamos la lista usando lista.append con el número en la variable num
    lista.append(num)


maximo=max(lista)
minimo=min(lista)
#for n in lista:

#imprimimos máximo
print("Max:",maximo)
#imprimimos mínimo
print("Min:",minimo)