#Realiza un programa que pida 8 números enteros y los almacene en una lista. 
# A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.

#creamos la una lista 
lista=[]
#usamos un for para recorrer 10 posiciones(de 0 a 9)
for i in range(8):
    #pedimos al usuario un número y lo guardamos en la variable num
    num=int(input("Introduce un número "+str((i+1))))
    #rellenamos la lista usando lista.append con el número en la variable num
    lista.append(num)

#for para recorrer la lista
for n in lista:
    #si es divisible por 2...
    if(n%2==0):
        #será par
        print(str(n),"Par")
    #en cualquier otro caso
    else:
        #será impar
        print(str(n),"Impar")