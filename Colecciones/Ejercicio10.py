#Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
#El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. 
#Para ello, cada vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.

# Conjuntos
conjunto1 = ["e","i","k","m","p","q","r","s","t","u","v"]
conjunto2 = ["p","v","i","u","m","t","e","r","k","q","s"]

# Crear diccionario usando zip
diccionario = dict(zip(conjunto1, conjunto2))

#pedimos frase al usuario y guardamos variable
frase=input("Introduce una frase a cifrar")
#creamos variable frase cifrada inicializada sin nada
fraseCif=""
#for para recorrer por letras la frase
for letra in frase: 
    #concatenamos a fraseCif un get del diccionario que si encuentra la clave le asina el valor
    fraseCif+=diccionario.get(letra,letra)

# Mostrar el diccionario
print(fraseCif)