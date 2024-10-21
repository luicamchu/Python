
from factorial import *

def main():
    numero1:int = int(input("Introduce un valor para el Número 1: "))
    numero2:int = int(input("Introduce un valor para el Número 2: "))

    print("El resultado factorial del Número 1 es : " + str(factorial(numero1)))
    print("El x del Número 1 y Número 2 es : " + str(numero_c(numero1, numero2)))

if __name__ == "__main__":
    main()
