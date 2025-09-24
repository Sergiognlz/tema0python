# Pedir dos números y mostrarlos ordenados de menor a mayor.

# pedimos número 1 y lo alamcenamos en variable numero1
numero1=int(input("Introduce número 1"))
# pedimos número 2 y lo almacenamos en variable numero2
numero2=int(input("Introduce número 2"))
#guardamos en una variable menor el menor(min) de los dos números
menor=min(numero1,numero2)
#guardamos en una variable mayor el mayor(max) de los dos números
mayor=max(numero1,numero2)
#imprimimos menor y mayor junto con un mensaje de texto
print("menor=",menor,"mayor=",mayor)
