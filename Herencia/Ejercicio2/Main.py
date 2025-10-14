from Empleado import Empleado
from Operario import Operario
from Directivo import Directivo
from Oficial import Oficial
from Tecnico import Tecnico 

def main():
   
    empleado1=Empleado('Juan Perez')
    operario1=Operario('Ana Gomez')
    directivo1=Directivo('Carlos Lopez')
    oficial1=Oficial('Luis Martinez')
    tecnico1=Tecnico('Marta Sanchez')

    print(empleado1)
    print(operario1)
    print(directivo1)  
    print(oficial1)  
    print(tecnico1)

if __name__ == "__main__":
    main()



