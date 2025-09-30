#Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

#importamos clase math
import math

#pedimos número al usuario y lo guardamos en una variable num
num=int(input("Introduce un número entero positivo"))

#si el número es menor que 2...
if num<2:
   #no será primo(no hay número primos menores de 2)
   primo=False
#si el número es 2...
elif num==2:
   #será primo(2 es primo)
   primo=True
#si el número es par(divisible por 2)...
elif num%2==0:
   #no será primo(cualqueir número divisible no será primo)
   primo=False
#en cualquier otro caso
else:
   #límite será la raíz cuadrada de n
   limite=int(math.sqrt(num))
   #Asumimos que el número será primo hasta que demostremos lo contrario
   primo=True
   #bucle for para recorrer los números desde el 3 hasta la raíz cuadrada+1(para que esté incluída) de 2 en dos para saltar pares
   for n in range(3,(limite+1),2):
     #si el número se puede dividir entre algún número... 
        if num%n==0:
            #no será primo
            primo=False
  
#si primo es true
if primo:
    #mensaje primo
   print("El número es primo")
#en cualquier otro caso
else:
   #no será primo
   print("El número NO es primo")