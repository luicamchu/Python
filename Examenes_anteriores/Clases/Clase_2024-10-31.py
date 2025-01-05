from collections import namedtuple
from datetime import date, datetime, time
from typing import Literal, NamedTuple, NewType, Sequence,Tuple,List,Set,Dict,Union,Any,Optional,Callable,Iterable

# “Tipando” con la librería typing

# La ventaja del módulo typing es proporcionar anotaciones de tipos más claras y específicas
# para mejorar la legibilidad y el análisis estático del código

# Nombre = NamedTuple('nombre',[('nombre_campo1', tipo), ('nombre_campo2', tipo), ….])
Vuelo = NamedTuple("Vuelo",[('destino', str),('precio', float),('num_plazas', int), \
('num_pasajeros', int),('código', str), ('fecha', date), \
('duración', int), ('hora', time), ('velocidad', float), \
('escalas', List[str]), ('económico', bool)])

# namedtuple vs NamedTuple:
Entreno = namedtuple ("Entreno", "tipo, fechahora, ubicacion, duracion, \
calorias, distancia, frecuencia, compartido")
# IMPORTANTE: todos son de tipo str
Entreno = NamedTuple ('Entreno', [('tipo', str), ('fechahora', datetime), \
('ubicacion', str), ('duracion', int), \
('calorias', float), ('distancia', float), \
('frecuencia', int), ('compartido', bool)])

# Sintaxis para Tuplas
# Tuple [tipo1, tipo2, tipo3, tipo4, …]                  
# Ejemplo:
def funcion1 (t:Tuple[int, float, Tuple[str, int]]) -> None:                    
    print(t)
funcion1((1, 2.3, ("bye", 3)))

# Sintaxis para Listas
# List [tipo]
# Ejemplos:             
def funcion2 (l: List[int]) -> None:
    print(l)
funcion2([1,2,3]) #  Salida: [1, 2, 3]

def funcion3 (l: List[Tuple[int, float]]) -> None:
    print(l)
funcion3([(1,2.3),(4,5.6)]) #  Salida: [(1, 2.3), (4, 5.6)]

# Sintaxis para Conjunto
# Set [tipo]
# Ejemplos:
def funcion4(c:Set[int]) -> None:
    print(c)
funcion4({1,2,3}) #  Salida: {1, 2, 3}

def funcion5(c:Set[Tuple[int, float]]) -> None:
    print(c)
funcion5({(1,2.3),(4,5.6)}) #  Salida: [(1, 2.3), (4, 5.6)]

# Sintaxis para Diccionarios
# Dict [tipo de la clave, tipo del valor]
# Ejemplo:
def funcion6 (d:Dict[int, str]) -> None:
    print(d)
funcion6({1:'Manolo', 2:'Paula'}) #  Salida: {1: 'Manolo', 2: 'Paula’}

def funcion7 (d:Dict[int, Set[Tuple[str, float]]]) -> None:
    print(d)
funcion7({1:{('Manolo',82.1), ('Paula',93.2)}, 2:{('Ana',50.3), ('Lucas',77.7)}})

# Sintaxis para Union (un mismo campo pueda recibir más de un tipo diferente)
# Union [tipo1, tipo2, tipo3, ...]
# Ejemplo:
def funcion8 (dato:Union[str,int]) -> None:
    print(dato)
funcion8("Hola") #  Salida: Hola
funcion8(25) #  Salida: 25

def funcion8 (dato:str|int="Adiós") -> None:# dato puede ser de tipo str o int, si no recibe nada tiene un valor pot defecto
    print(dato)
funcion8("Hola") #  Salida: Hola
funcion8(25) #  Salida: 25
funcion8() #  Salida: Adiós

# Método: isinstance
print(isinstance("a", str))
print(isinstance(1, str))

# Sintaxis para Any
# Any
# Ejemplo:
def funcion9(dato: Any) -> Any:
    if isinstance(dato, str): # Si es una cadena
        return dato.upper() #  Devolvemos la cadena en mayúsculas
    elif isinstance(dato, int): #  Si es un entero
            return dato * 2 #  Devolvemos el doble del valor
    else: #  Si es otro tipo de dato
        return dato #  Simplemente lo devolvemos
print(funcion9("hola")) #  Salida: HOLA
print(funcion9(10)) #  Salida: 20
print(funcion9([1, 2, 3])) #  Salida: [1, 2, 3]

# Sintaxis para Optional (útil para indicar que un valor puede ser de un tipo específico o None)
# Optional [tipo]
# Ejemplo:
def buscar_elemento(lista:list, elemento:int) -> Optional[int]:
    if elemento in lista:
        return elemento
    else:
        return None
res1 = buscar_elemento([1, 2, 3, 4], 3)
print(f"{res1}") #  Salida: 3
res2 = buscar_elemento([1, 2, 3, 4], 5)
print(f"{res2}") #  Salida: None

# Sintaxis básica para Callable (para representar una función o un método que puede ser llamado)
# Callable [[Argumento1Tipo, Argumento2Tipo, ...], TipoDeRetorno]
# Ejemplo:
def sumar(x:int, y:int) -> int: #  Función sumar que coinciden con tipo Operacion
    return x + y
def multiplicar(x:int, y:int) -> int: #  Función multiplicar que coinciden con tipo Operacion
    return x * y
Operacion = Callable[[int, int], int] #  tipo Callable que toma 2 enteros y devuelve un entero
# Función que toma otra función como argumento
def funcion(a:int, b:int, operacion:Operacion) -> int:
    return operacion(a, b)
# Usamos aplicar_operacion con diferentes funciones
res1 = funcion(3, 5, sumar)
print(f"Resultado de la suma: {res1}") #  Salida: 8
res2 = funcion(3, 5, multiplicar)
print(f"Resultado de la multiplicación: {res2}") #  Salida: 15

# Sintaxis para Iterable (representa cualquier objeto que se puede iterar)
# Iterable [Tipo]
# Ejemplo:
def sumarDatos(numeros:Iterable[int]) -> int:
    total = 0
    for n in numeros:
        total += int(n)
    return total
cadenaNumeros = "012"
listaNumeros = [3, 4, 5]
tuplaNumeros = (6, 7, 8)
conjuntoNumeros = {9, 10, 11}
print(sumarDatos(cadenaNumeros)) # Salida: 3
print(sumarDatos(listaNumeros)) # Salida: 12
print(sumarDatos(tuplaNumeros)) # Salida: 21
print(sumarDatos(conjuntoNumeros)) # Salida: 30

# Sintaxis para Literal
# Literal [str1, str2, str3, ...]
# Ejemplo:
def colorear(objeto:str, color:Literal["rojo", "verde", "azul"]) -> str:
    return f"El '{objeto}' debe pintarse de color {color}."
print(colorear("cuadrado", "rojo")) #  Salida: El 'cuadrado' debe pintarse de color rojo.
print(colorear("rombo", "verde")) #  Salida: El 'rombo' debe pintarse de color verde.

# Otros tipos comunes:
# Sequence [Tipo] Representa secuencia inmutable de elementos, como listas, tuplas y cadenas
# Ejemplo:
def promedio(numeros:Sequence[float]) -> float:
    total, cantidad = sum(numeros), len(numeros)
    return total / cantidad if cantidad > 0 else 0.
listaNumeros, tuplaNumeros, cadenaNumeros = [1.5, 2.5, 3.5, 4.5], (10.0, 20.0, 30.0, 40.0), set()
print(promedio(listaNumeros)) #  Salida: 3.0
print(promedio(tuplaNumeros)) #  Salida: 25.0
print(promedio(cadenaNumeros)) #  Salida: 0.0

# NewType ('NuevoTipo', TipoExistente) Define un nuevo subtipo de un tipo existente
# Ejemplo:
# Definir nuevos tipos
UserID = NewType('UserID', int)
ProductID = NewType('ProductID', str)
user_id = UserID(1234)
product_id = ProductID("ES4102")
print(str(user_id) + " propietario de " + product_id)
