from typing import List, Callable

# Tipo para la matriz
Matriz = List[List[int]]
def crearMatrizHomogenea(filas:int, columnas:int, valor_inicial:int = 0) -> Matriz:
 """ Crear matriz homogénea, de num. filas x columnas, e inicializada con valor_inicial """
 #pass
 return [[valor_inicial for _ in range(columnas)] for _ in range(filas)]

def crearMatriz(datos: Matriz) -> Matriz:
 """ Crear una matriz a partir del parámetro de entrada """
 #pass
 filas = len(datos)
 columnas = len(datos[0]) if filas > 0 else 0

 if filas != columnas:
  raise ValueError("La matriz debe de ser cuadrada")
 
 #opcion 1
 matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

 #opcion 2, utilizar el metodo anterior
 matriz = crearMatrizHomogenea(filas, columnas)
 #otra forma de hacerlo
 for i in range(filas):
  for j in range(columnas):
   matriz[i][j] = datos[i][j]
 return matriz
 

def es_cuadrada(matriz: Matriz) -> bool:
 """ Verificar si una matriz es cuadrada """
 #pass
 filas_m = len(matriz[0])
 columnas_m = len(matriz)
 
 if filas_m != columnas_m:
  return False
 else:
  return True
 #return (filas_m == columnas_m)

 
def es_simetrica(matriz: Matriz) -> bool:
 """ Verificar si una matriz es cuadrada y es simétrica """
 #pass
 if es_cuadrada(matriz):
  return es_cuadrada(matriz)
 
 for i in range(matriz):
  for j in range(matriz[0]):
   if matriz[i][j] != matriz[j][i]:
    return True
   else: 
    return False
   
 
def sumarMatrices(matriz1: Matriz, matriz2: Matriz) -> Matriz:
 """ Sumar 2 matrices cuadradas del mismo tamaño """
 #pass
 if es_cuadrada(matriz1) and es_cuadrada(matriz2):
  return es_cuadrada(matriz1) and es_cuadrada(matriz2)
 
 return [[matriz1[i][j] + matriz2[i][j] for i in range(matriz2)] for j in range(matriz2[0])]

def restarMatrices(matriz1: Matriz, matriz2: Matriz) -> Matriz:
 """ Restar 2 matrices cuadradas del mismo tamaño """
 #pass
 if es_cuadrada(matriz1) and es_cuadrada(matriz2):
  return es_cuadrada(matriz1) and es_cuadrada(matriz2)
 
 return [[matriz1[i][j] - matriz2[i][j] for i in range(matriz2)] for j in range(matriz2[0])]

def multiplicarMatrices(matriz1: Matriz, matriz2: Matriz) -> Matriz:
 """ Multiplicar 2 matrices cuadradas y compatibles para la multiplicación """
 #pass
 filas_m1 = len(matriz1[0])
 columnas_m1 = len(matriz1)

 filas_m2 = len(matriz2[0])
 columnas_m2 = len(matriz2)
 
 if (columnas_m1 != filas_m1):
  raise("Las matrices no son compatibles para la multiplicacion")
 
 resultado = crearMatrizHomogenea(filas_m1, columnas_m2)
 #montar una matriz con valor 0, contador en forma de matriz.
 for i in range(filas_m1):
  for j in range(columnas_m2):
   for k in range(columnas_m1):
    resultado[i][j] += matriz1[i][k] * matriz2[k][j]
 return resultado

def trasponerMatriz(matriz: Matriz) -> Matriz:
 """ Obtener traspuesta de la matriz cuadradas indicada """
 #pass
 filas = len(matriz)
 columnas = len(matriz[0])

 return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

def trazaMatriz(matriz: Matriz) -> int:
 """ Calcular La traza de una matriz cuadrada """
 #pass
 return sum(matriz[i][i] for i in range(len(matriz)))

def aplicarOperacion(matriz1: Matriz, matriz2: Matriz, operacion:Callable[[Matriz, Matriz],
Matriz]) -> Matriz:
 """ Aplicar una operación matricial recibida como parámetro """
 #pass
 #  
