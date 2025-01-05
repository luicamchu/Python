from matrices import *

if __name__ == '__main__':

 matriz1 = crearMatrizHomogenea(3, 3, 1)
 print("\nMatriz 1:")
 for fila in matriz1:
  print(fila)

 datos1 = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

 datos2 = [[4, 5, 6],
 [7, 8, 9],
 [1, 2, 3]]

 datos3 = [[7, 8, 9],
 [1, 2, 3],
 [4, 5, 6]]

 matriz2 = crearMatriz(datos1)
 matriz3 = crearMatriz(datos2)
 matriz4 = crearMatriz(datos3)

 print("\nMatriz 2:")
 for fila in matriz2:
  print(fila)
 print("\nMatriz 3:")
 for fila in matriz3:
  print(fila)

 print("\nMatriz 4:")
 for fila in matriz4:
  print(fila)

 # Suma de matrices
 matriz_suma = sumarMatrices(matriz2, matriz1)
 print("\nSuma de Matriz 2 y Matriz 1:")
 for fila in matriz_suma:
  print(fila)
 # Resta de matrices
 matriz_resta = restarMatrices(matriz2, matriz1)
 print("\nResta de Matriz 2 y Matriz 1:")
 for fila in matriz_resta:
  print(fila)
 # Multiplicación de matrices
 matriz_multiplicada = multiplicarMatrices(matriz2, matriz1)
 print("\nMultiplicación de Matriz 2 y Matriz 1:")
 for fila in matriz_multiplicada:
  print(fila)
 # Trasposición de matriz
 matriz_traspuesta = trasponerMatriz(matriz2)
 print("\nTraspuesta de Matriz 2:")
 #for fila in matriz_traspuesta:
 print(matriz_traspuesta)

 print(f"\nTraza de la Matriz2: {trazaMatriz(matriz2)}")
 print("\n ****** Callable ****** ")
 print("\n ** Sumar Matriz 3 y Matriz 4, usando parámetro de tipo Callable **")
 matriz_suma1 = aplicarOperacion(matriz3, matriz4, sumarMatrices)
 for fila in matriz_suma1:
  print(fila)

 print("\n ** Restar Matriz 3 y Matriz 4, usando parámetro de tipo Callable **")
 matriz_resta1 = aplicarOperacion(matriz3, matriz4, restarMatrices)

 for fila in matriz_resta1:
  print(fila)

print("\n ** Multiplicar Matriz 3 y Matriz 4, usando parámetro de tipo Callable **")
matriz_multiplicada1 = aplicarOperacion(matriz3, matriz4, multiplicarMatrices)

for fila in matriz_multiplicada1:
 print(fila) 
