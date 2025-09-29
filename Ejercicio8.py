#Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   #*
  #* *

#pedimos número al usuario y lo guardamos en una variable num
num=int(input("Introduce un número entero positivo"))
  

   
for i in range(1, num + 1):
    # Espacios iniciales para centrar la pirámide
    print(" " * (num - i), end="")
    # Asteriscos con espacio entre ellos
    print("* " * i)


  
    