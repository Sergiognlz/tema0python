#Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación para cada letra, como en el Scrabble. 
# El programa le pedirá una palabra al usuario y se mostrará por pantalla la puntuación que tiene la palabra en total.

#creamos diccionario cuya clave es una letra y el valor su puntuación
puntuacion= {
    "A": 1, "B": 3, "C": 3, "CH": 5, "D": 2, "E": 1, "F": 4, "G": 2,
    "H": 4, "I": 1, "J": 8, "K": 8, "L": 1, "LL": 8, "M": 3, "N": 1,
    "Ñ": 8, "O": 1, "P": 3, "Q": 5, "R": 1, "RR": 8, "S": 1, "T": 1,
    "U": 1, "V": 4, "X": 8, "Y": 4, "Z": 10
}

#pedimos palabra al usuario y la guardamos en variable
palabra=input("Bienvendio a Scrabble. Escribe una palabra")
#variable puntos inicializada a 0
puntos=0
#for para recorrer palabra en mayúscula por letra
for letra in palabra.upper():
    #si la letra que recorremos está en el diccionario...
    if(letra in puntuacion):
        #asignamos a puntos el valor de esa letra
        puntos+=puntuacion[letra]
#imprimimos puntos 
print("Puntos: "+str(puntos))