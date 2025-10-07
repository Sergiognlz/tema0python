# Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo. 
# Añade los siguientes constructores:
# Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
# Con el DNI, nombre y el saldo inicial.
# Las operaciones típicas de una cuenta corriente son:
# Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, si existe saldo suficiente. Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
# Ingresar dinero: se incrementa el saldo.
# Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos cuentas corrientes son iguales si tienen el mismo DNI. Las cuentas corrientes se ordenarán de menor a mayor por el saldo.


class CuentaCorriente:
    def __init__(self, dni, saldo, nombre=""):
        self.dni=dni
        self.saldo=saldo


    def __init__(self, dni, saldo, nombre):
        self.dni=dni
        self.nombre=nombre
        self.saldo=saldo

    def sacar_dinero(self,saldo):
        exito=False

        if(self.saldo-saldo>=self.saldo):
            exito=True

        return exito 
    
    def ingreso(self,saldo):
        self.saldo+=saldo

    def __str__(self):
        return ("DNI:",self.dni,"Nombre:",self.nombre, "Saldo:",self.saldo)
        

    def __eq__(self, dni):
        iguales=False
        if(self.dni==dni):
            iguales=True
        return iguales
    
    def __lt__(self,saldoOtra):
       
        return self.saldo<saldoOtra

class Main:

    cuenta1 = CuentaCorriente("30250815L",1000)

    print(cuenta1)



    
