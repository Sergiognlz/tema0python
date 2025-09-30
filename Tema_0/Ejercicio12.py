#Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos.
# Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 
# 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división.
#  La función devolverá el resultado de la operación mediante un número real.

#creamos función calculadora y le pasamos los dos números y la opción
def calculadora(num1, num2, opcion):
    #usamos match que funciona como un switch
    match opcion:
        #caso 1
        case 1:
            #suma
            res=num1+num2
            #caso 2
        case 2:
            #resta
            res=num1-num2
            #caso 3
        case 3:
            #multiplicación
            res=num1*num2
            #caso 4
        case 4:
            #división
            res=num1/num2
            #default
        case _: 
            #mensaje error
            res=("La opción introducida no es válida")       

#devolvemos respuesta
    return res

#pedimos num1 al usuario y guardamos en num1
num1=int(input("Introduce num1"))
#pedimos num2 al usuario y guardamos en num2
num2=int(input("Introduce num2"))
#pedimos opción al usuario y guardamos en opción
opcion=int(input("Introduce opción: 1 sumar, 2, restar, 3 multiplicar, 4 dividir"))

#imprimimos lo que devuelve la función calculadora y le pasamos los 3 parámetros
print(calculadora(num1,num2,opcion))
