#Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
# Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, antes de acabar,
#  mostrará la suma de los números positivos introducidos por el usuario.


#declaramos variable suma donde guardaremos la suma de los números. Por defecto a 0
suma=0
#pedimos un número y lo guardamos en una variable número
numero=int(input("Introduce un número"))
#bucle while que se repetirá hasta que número sea un valor negativo
while numero>0:
   #suma será la suma de los números
    suma+=numero
    #volvemos a pedir número
    numero=int(input("Introduce un número"))
#imprimimos suma
print("suma:",suma)