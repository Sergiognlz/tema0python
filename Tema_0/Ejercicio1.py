# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

# en una variable número guardamos un número que pedimos al usuario
numero=int(input("Introduce un número?"))
#si el número fuese 0...
if numero==0:
    #mensaje de que 0 no es par ni impar
    print("El número es 0 y no es par ni impar")

#en caso contrario ...
else:
    # en una variable respuesta guardamos una cadena que nos diga sin es par o no en base a si el resto de dividir por 2 es 0
    res= "Es par" if(numero%2==0) else "Es impar"
    # imprimimos respuesta
    print(res)