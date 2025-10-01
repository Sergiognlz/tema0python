#Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres de los productos y los valores son las cantidades vendidas.
#  El programa debe permitir al usuario agregar nuevas ventas y calcular el total de ventas para un producto específico. Implementa un menú con ambas opciones. 

#creamos diccionario ventas
ventas={}
#creamos función agregar y le pasamos nombre y número de ventas
def agregar (nombre, numventa):
    #si el producto ya está en el diccionario
    if(nombre in ventas):
        #se incrementa en tantas unidades como numventa
        ventas[nombre]+=numventa
    #si no...
    else:
        #se añade con numventa como valor
        ventas[nombre]=numventa
    #devolvemos mensaje de éxito
    return "La venta se ha añadido con éxito"
#creamos función buscar y le pasamos el nombre como parámetro
def buscar(nombre):
    #si el producto existe...
    if(nombre in ventas):
        #guarda en respuesta el nombre del producto y la cantidad
        res=nombre+": "+str(ventas[nombre])
    #si no existe...
    else:
        #guarda en respuesta un mensaje de que no existe o no tiene ventas
        res="El producto no existe o no tiene ventas"
    #devuelve la respuesta
    return res

#menú de programa
print("Menú de ventas")
print("1. Agregar venta")
print("2. Calcular el total de ventas de un producto")
print("0. Salir")
#pedimos opción al usuario y la guardamos en una variable
opcion=int(input("Introduce la opción deseada"))
#bucle while que se repetirá hasta que la opción elegida no sea 0
while(opcion!=0):
    #match con opciones
    match opcion:
        #caso 1: agregar nueva venta
        case 1:
            #pedimos nombre y guardamos en variable
            nombre=input("Introduce el nombre del producto")
            #pedimos número de venta y guardamos en variable
            numventa=int(input("Introduce el numero de productos a vender"))
            #imprimimos la respuesta resultante de llamar a la función agregar
            print(agregar(nombre,numventa))
        #caso 2: buscar
        case 2:
            #pedimos nombre y guardamos en variable
            nombre=input("Introduce el nombre del producto")
            #imprimimos resultado de llamar a la función buscar
            print(buscar(nombre))
        #default
        case _:
            #mensaje error
            print("La opción es errónea")
    #menú again
    print("1. Agregar venta")
    print("2. Calcular el total de ventas de un producto")
    print("0. Salir")
    #pedimos opción again
    opcion=int(input("Introduce la opción deseada"))

#mensaje de saliendo
print("saliendo")