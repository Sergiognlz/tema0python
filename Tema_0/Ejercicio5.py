#Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.

#pedimos número objetivo al usuario y lo guardamos en una variable numObj
numObj=int(input("Introduce un número objetivo para aprender a contar"))


#bucle for que recorrerá los números desde el 1 hasta alcanzar el objetivo+1 para que esté incluído
for num in range(1,numObj+1):
    #imprimimos cada número
    print(num)