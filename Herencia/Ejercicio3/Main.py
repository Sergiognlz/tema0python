from Producto   import Producto
from Perecedero import Perecedero
from NoPerecedero import NoPerecedero

def main():
   
        producto1=Perecedero("Leche", 1.50, 2)
        producto2=Perecedero("Yogur", 0.80, 1)
        producto3=NoPerecedero("Arroz", 2.00, "Alimento")
        producto4=NoPerecedero("Detergente", 3.50, "Limpieza")

        

        print(f"{producto1} Precio final: {producto1.Calcular(3)} €")
        print(f"{producto2} Precio final: {producto2.Calcular(5)} €")
        print(f"{producto3} Precio final: {producto3.Calcular(2)} €")
        print(f"{producto4} Precio final: {producto4.Calcular(1)} €")
    

if __name__ == "__main__":
    main()