from matricesT import * 
from fractions import Fraction 
 
def imprimirMatriz(matriz): 
    for fila in matriz:  
        print(' '.join(str(elemento) for elemento in fila)) 
 
if __name__ == '__main__': 
     
    matriz1 = crearMatrizHomogenea(3, 3) 
     
    datos1 = [[Fraction(1,1), Fraction(2,1), Fraction(3,1)], 
              [Fraction(4,1), Fraction(5,1), Fraction(6,1)], 
              [Fraction(7,1), Fraction(8,1), Fraction(9,1)]] 
 
    datos2 = [[Fraction(4,2), Fraction(5,2), Fraction(6,2)], 
              [Fraction(7,2), Fraction(8,2), Fraction(9,2)], 
              [Fraction(1,2), Fraction(2,2), Fraction(3,2)]]     
     
    datos3 = [[Fraction(7,3), Fraction(8,3), Fraction(9,3)], 
              [Fraction(1,3), Fraction(2,3), Fraction(3,3)], 
              [Fraction(4,3), Fraction(5,3), Fraction(6,3)]] 
 
    matriz2 = crearMatriz(datos1) 
    matriz3 = crearMatriz(datos2) 
