#Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa 
# como parámetro de entrada corresponde con una vocal.

#creamos función detectar vocal y le pasamos un string 
def detectarVocal(char):
    #si en el string se encuentra alguna vocal...
    if(char in "aeiou"):
        #será una vocal
        vocal=True
    #en caso contrario
    else:
        #no será una vocal
        vocal=False
    #devolvemos si es una vocal
    return vocal
#pedimos un carácter al usuario
char = input("Introduce un carácter: ")

# Verificar que tenga longitud 1
if len(char) == 1:
    #si es correcto imprime la letra
    print("Letra:", char)
#si no...
else:
    #mensaje de error
    print("Error: debes introducir un solo carácter")
#if y llamamos a la función
if(detectarVocal(char)):
    #si es vocal imprime un mensaje
    print("Es una vocal")
    #si no es vocal...
else:
    #mensaje informativo
    print("No es una vocal")