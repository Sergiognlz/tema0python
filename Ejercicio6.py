#Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.

#pedimos número al usuario y guardamos en una variable número
num=int(input("Introduce un número para calcular su factorial"))
#creamos una variable factorial por defecto a 1 para multiplicar sin cambios
fac=1
#for para recorrer hasta el número objetivo+1 para que lo incluya
for n in range(1,num+1):
   #concatenamos multiplicaciones del número en el que nos encontremos: ejem 1x1x2x3x4x5=120 y guardamos en la variable factorial
   fac*=n
#imprimimos factorial
print(fac)