#Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

#creamos la una lista 
lista=[]
#usamos un for para recorrer 10 posiciones(de 0 a 9)
for i in range(10):
    #pedimos al usuario un número y lo guardamos en la variable num
    num=int(input("Introduce un número "+str((i+1))))
    #rellenamos la lista usando lista.append con el número en la variable num
    lista.append(num)

#ordenamos la lista de manera inversa usando sort y reverse=True entre paréntesis
lista.sort(reverse=True)
#imprimimos lista
print(lista)

