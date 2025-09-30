#Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. 
# Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, 
# y pásalos como parámetros de entrada de la función.

#creamos función mostrarNumeros y le pasamos dos números
def mostrarNumeros(num1, num2):
    #recorremos con un for desde num1 hasta num2+1(para que llegue hasta él)
    for i in range(num1,(num2+1)):
        #imprimimos el número actual
        print(i)

#pedimos número de inicio al usuario y guardamos en num1
num1=int(input("Introduce el número de partida"))
#pedimos número final al usuario y guardamos en num2
num2=int(input("Introduce el número objetivo"))
#llamamos a la función mostrarNumeros y le pasamos los dos números
mostrarNumeros(num1,num2)