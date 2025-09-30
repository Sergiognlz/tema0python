#Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.


#declaramos la función numeroMax y le pasamos dos números por parámetros
def numeroMax(num1,num2):

    #devolvemos el mayor(max) de ambos números
    return max(num1,num2)


#pedimos num1 al usuario
num1=int(input("Introduce el primer número"))
#pedimos num2 al usuario
num2=int(input("Introduce el segundo número"))

#imprimimos mensaje más llamada a la función y le pasamos los números
print("El número mayor es",numeroMax(num1,num2))

