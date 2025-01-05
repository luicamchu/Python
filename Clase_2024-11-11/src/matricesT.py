from typing import List, TypeVar, Callable 
 
# Definimos un tipo para el contenido de la matriz  
T = TypeVar('T') 
 
# Tipo para la matriz 
MatrizT = List[List[T]] 
 
def crearMatrizHomogenea(filas:int, columnas:int, valor_inicial:int = 0) -> MatrizT: 
    """ Crear matriz homogénea, de num. filas x columnas, e inicializada con valor_inicial """ 
    #pass 
    return [[valor_inicial for _ in range(filas)] for _ in range(columnas)]
 
def crearMatriz(datos: MatrizT) -> MatrizT: 
    """ Crear una matriz cuadradas a partir del parámetro de entrada) """ 
    pass 
 
def es_cuadrada(matriz: MatrizT) -> bool:  
    """ Verificar si una matriz es cuadrada """  
    pass 
     
def es_simetrica(matriz: MatrizT) -> bool:  
    """ Verificar si una matriz es cuadrada y es simétrica """  
    pass 
 
def sumarMatrices(matriz2: MatrizT, matriz1: MatrizT) -> MatrizT:         
    """ Sumar 2 matrices cuadradas del mismo tamaño """ 
    pass 
 
def restarMatrices(matriz2: MatrizT, matriz1: MatrizT) -> MatrizT: 
    """ Restar 2 matrices cuadradas del mismo tamaño """ 
pass 
 
def multiplicarMatrices(matriz2: MatrizT, matriz1: MatrizT) -> MatrizT:         
    """ Multiplicar 2 matrices cuadradas y compatibles para la multiplicación """ 
    pass 
 
def trasponerMatriz(matriz: MatrizT) -> MatrizT: 
    """ Obtener traspuesta de la matriz cuadradas indicada """ 
    pass 
 
def trazaMatriz(matriz: MatrizT) -> T: 
   """ Calcular La traza de una matriz cuadrada """     
pass 
 
def aplicarOperacion(matriz4: MatrizT, matriz3: MatrizT, operacion:Callable[[MatrizT, MatrizT], 
MatrizT]) -> MatrizT:  
    """ Aplicar una operación matricial recibida como parámetro """  
    pass