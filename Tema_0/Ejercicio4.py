#Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
# Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, 
# según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde 
# (introduciendo un -1).

#importamos la clase random
import random

#pedimos un número y lo guardamos en una variable número además de presentar las instrucciones del juego 
numero=int(input("Juego número secreto. Introduce un número e intenta adivinarlo o ríndete con -1"))
#generamos un número aleatorio entre 1 y 100 y lo guardamos en la variable numSecreto
numSecreto=random.randint(1,100)

#creamos bucle while que se repetirá hasta que el usuario acierte el número secreto
while numero!=numSecreto and numero!=-1:
    #si el número introducido es mayor que el secreto...
    if numero>numSecreto:
        #mensaje número mayor
        print("El número es mayor")
    #en cualquier otro caso...
    else:
        #mensaje número menor
        print("El número es menor")
    #pedimos otra vez el número
    numero=int(input("Introduce un número e intenta adivinarlo o ríndete con -1"))
#si se ha rendido
if numero==-1:
    #mensaje de rendición
    print("Te has rendido, eres un pargüela")
#en cualquier otro caso    
else:
    #mensaje de victoria
    print("Has ganado. El número secreto era",numSecreto)

