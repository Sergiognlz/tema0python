#Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. 
# La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. 
# Crea un menú para las distintas opciones e implementa una función para cada opción.

#creamos diccionario contactos
contactos={}

#función agregar y le pasamos nombre y télefono a agregar por parámetros
def agregar(nombre,telefono):
    #si el nombre ya existe en el contacto..
    if nombre in contactos:
        #exito será false y fallará
        exito=False
    #si no existe...
    else:
        #lo creará
        contactos[nombre]=telefono
        #y el proceso será exitoso
        exito=True
    #devolvemos si ha tenido éxito o no
    return exito

#función eliminar y le pasamos nombre a eliminar por parámetro
def eliminar(nombre):
    #si el nombre está en el diccionario..
    if nombre in contactos:
        #lo borra
        del contactos[nombre]
        #operación exitosa
        exito=True
    #en caso de que no exista el contacto...
    else:
        #operación falla
        exito=False
    #devolvemos si la operación tiene éxito o no
    return exito

#función buscar y le pasamos por parámetro el nombre a buscar
def buscar(nombre):
    #si el nombre está en el diccionario
    if nombre in contactos:
       #guardamos el valor asociada a la clave
       res=contactos[nombre]
    # sino...
    else:
        #guardamos en respuesta un mensaje que nos indica que el contacto no existe
        res="El contacto no existe"
    #devolvemos la respuesta
    return res

#menú del programa
print("Bienvenido a tu app de contactos. Introduce una opción:")
print("1. Agregar nuevo contacto")
print("2. Eliminar contacto existente")
print("3. Buscar contacto")
print("0. Salir")
#pedimos a usuario que introduzca la opción deseada y la guardamos en una variable opción
opcion=int(input("Introduce la opción deseada:"))
#bucle que se repite mientras la opción elegida no sea 0
while(opcion!=0):
#match con los casos
    match opcion:
        #caso 1: agregar nuevo contacto
        case 1:
            #pedimos nombre y guardamos en variable
            nombre=input("Introduce el nombre a guardar")
            #pedimos teléfono y los guardamos en variable
            telefono=input("Introduce el teléfono a guardar")
            #si la función agregar tiene éxito...
            if (agregar(nombre,telefono)):
                #mensaje de éxito
                print("Se agregó correctamente")
            #si falla
            else:
                #mensaje fallo
                print("No se ha podido agregar")
        #caso 2: eliminar contacto
        case 2:
            #pedimos nombre y lo guardamos en variable
            nombre=input("Introduce el nombre del contacto a eliminar")
            #si la función eliminar tiene éxito...
            if (eliminar(nombre)):
                #mensaje éxito
                print("Se eliminó correctamente")
            #si fracasa...
            else:
                #mensaje fallo
                print("No se ha podido eliminar")
        #caso 3: buscar contacto
        case 3:
              #pedimos nombre y guardamos en variable
              nombre=input("Introduce el nombre del contacto a buscar")
              #imprimimos el resultado de la función buscar
              print(buscar(nombre))
       
        #default
        case _:
            #mensaje error
            print("Opción errónea")

#menú del programa again
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("0. Salir")
    #pedimos opcion de nuevo
    opcion=int(input("Introduce la opción deseada:"))

 #caso 0: salir
print("Saliendo")


