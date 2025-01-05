palabras = ["satélite", "sol", "luna", "estrella", "marte", "júpiter"]

# 1. Filtrar palabras que tienen menos de 5 letras
palabras_filtradas = list(filter(lambda x: len(x) < 5, palabras))
print("Palabras filtradas:", palabras_filtradas) # ['sol', 'luna']

# 2. Convertir las palabras filtradas a mayúsculas
palabras_mayusculas = list(map(lambda x: x.upper(), palabras_filtradas))
print("Palabras en mayúsculas:", palabras_mayusculas) # ['SOL', 'LUNA']

# 3. Verificar si hay alguna palabra que comience con la letra 'S'
alguna_comienza_con_S = any(filter(lambda x: x.startswith('S'), palabras_mayusculas))
alguna_comienza_con_S = any(map(lambda x: x.startswith('S'), palabras_mayusculas))
print("¿Alguna palabra comienza con 'S'?", alguna_comienza_con_S) # True

# 4. Crear una lista de longitudes de las palabras filtradas
longitudes_palabras = list(map(lambda x: len(x), palabras_filtradas))
print("Longitudes de las palabras filtradas:", longitudes_palabras) # [3, 4]

# clave:valor

d1, d2, d3 = dict(), { }, ({ })
dic = dict(); dic = {}; dic = ({ })
dic = {"TI4":90, "TI2":51, "IS3":84, "TI3":72}
dic = {"Pepe", "Juana", "Margarita", "Antonio"}
#Las claves o valores pueden ser de cualquier tipo (de los estudiados) con la restricción
#que las claves NO pueden ser listas, conjuntos o diccionarios, pero si pueden ser tuplas.

#> Asociar personas con su edad.
dic1 = {"Eva":41, "Manuel":11, "Javier":24}
#> Asociar personas con tuplas que contienen su edad y provincia de nacimiento.
dic2 = {"Eva":(41,"Cádiz"), "Manuel":(11,"Sevilla"), "Javier":(24,"Murcia")}

#Acceder a los valores de un diccionario (dos formas de hacerlo)
#1. Acceso con el operador [ ] a través de las claves
print(dic1["Manuel"])
#print(dic1["José"]) #jose no existe, aborta
#2. Con el método get( ) a través de las claves
print(dic1.get("Manuel"))
print(dic1.get("José"))

# Se puede indicar un valor como 2º parámetro para el caso de que no exista la clave
print(dic2.get("Manuel", False))
print(dic2.get("José", 0))
print(dic2.get("José", False))

#Insertar o modificar datos de un diccionario
#   [nueva_clave] = valor
dic1["Isa"] = 20
print(dic1)
#   o [clave_existente] = nuevo_valor
dic1["Javier"] = 50
print(dic1)

# Método update
#Existe otra forma de “crear”, utilizando el método update()
dic2.update(dic1)
print(dic1)
print(dic2)

# Método clear
dic1 = {"Eva": 41, "Manuel": 11, "Javier": 24, "Ana": 28}
dic1.clear() 
print(dic1)

# Método del
#Eliminar datos de un diccionario
#del(diccionario[clave])
dic1 = {"Eva": 41, "Manuel": 11, "Javier": 24, "Ana": 28}
del(dic1["Manuel"])
#del(dic1["José"])
print(dic1)

#Si la clave no existe el programa aborta, ecomendable comprobar si existe o no la clave
clave = "José"
if dic1.get(clave, False) != False:
    del(dic1[clave])
#if dic1.has_key(clave)
    #del(dic1[clave])

n = "José"
if n in dic1.keys():
    del(dic1[n])
print(dic1)

# Método len
len(dic1)

# Método items
print(dic1.items())

#método para obtener una lista (list()) o un conjunto (set()):
result1 = list(dic1.items())
print(result1)
result2 = set(dic1.items())
print(result2)

for clave, valor in dic1.items():
    print(f"{clave}, {valor}")

# Método keys
print(dic1.keys())

#método para obtener una lista (list()) o un conjunto (set()):
result1 = list(dic1.keys())
print(result1)
result2 = set(dic1.keys())
print(result2)

# Método values
print(dic1.values())

#una lista (list()) o un conjunto (set()):
result1 = list(dic1.values())
print(result1)
result2 = set(dic1.values())
print(result2)

#Counter
from collections import Counter, defaultdict, namedtuple

dicc_cont = Counter("absbabbabbcc")
print(dicc_cont)#* el orden de aparición viene dado de mayor a menor frecuencia
# Salida: Counter({'b': 6, 'a': 3, 'c': 2, 's': 1})

#* Objetos iterables son aquellos que podemos recorrer usando un ciclo, entre ellos, las cadenas de
#texto o estructuras de datos como las listas, las tuplas o los diccionarios

lista = [12, 2, 4, 2, 12, 4, 5, 7, 8, 5, 4, 3, 10, 10, 10, 3, 3, 34, 7, 8, 9]
dic2 = Counter(lista)
print(dic2)

# Cuando el diccionario se ha creado con Counter():
print(dic2[6])# no aborta el programa; devuelve que hay 0 elementos
del(dic2[6])# no aborta el programa;
print(dic2)

dicc_cont = Counter("absbabbabbcc")
print(dicc_cont)

# Método most_common
print(dicc_cont.most_common(3))
print(dicc_cont.most_common(1))
print(dicc_cont.most_common(1)[0])
print(dicc_cont.most_common(1)[0][0])

palabras = ["kiwi", "pera", "melón", "mango", "pera", "kiwi", "piña", "kiwi", "piña"]

# Obtener diccionario que contenga cuantas veces aparece cada valor de una lista
lista = ['a','b','c','a','b','b','z','a','b','c']
dic = dict()
dic2 = dict()

#OPCIÓN 1
for letra in lista: # Se va recorriendo el contenedor (con un for)
# Se consulta si el elemento que será la clave ya está en el diccionario
    if letra not in dic:
        dic[letra] = 1 # Si no está se inserta una nueva pareja clave-valor (letra-1)
    else: # Si ya está se actualiza el valor
        dic[letra] += 1 # Esto es lo mismo que dic[letra] = dic[letra] + 1
print(dic)

#OPCIÓN 2
for letra in lista: # Se va recorriendo el contenedor (con un for)
    # Se consulta si el elemento que será la clave ya está en el diccionario
    if letra not in dic2:
        dic2[letra] = 0 # Se crea ya el elemento clave-valor (con el valor neutro)
    dic2[letra] += 1 # Esto es lo mismo que dic[letra] = dic[letra] + 1
print(dic2)

#Obtener diccionario, donde a cada letra de namedtaple, le haga corresponder una
#lista con los valores asociados

Par = namedtuple("pareja", "letra, numero")
lista = [Par("z",21),Par("a",62),Par("J",7),Par("b",56),Par("c",90),Par("z",21), \
Par("a",1),Par("b",10),Par("b",2),Par("a",21)]

# OPCIÓN 1
dic = dict()
for p in lista:
    if p.letra not in dic:
        dic[p.letra] = [p.numero]
    else:
        dic[p.letra] += [p.numero] # Es lo mismo que dic[p.letra].append(p.numero)
print(dic)

# OPCIÓN 2
dic = dict()
for p in lista:
    if p.letra not in dic:
        dic[p.letra] = list() # Valor neutro de listas (una lista vacía)
    dic[p.letra] += [p.numero] # Es lo mismo que dic[p.letra].append(p.numero)
print(dic)

#defaultdict
lista_tupla=[('a',1),('b',3),('a',4),('c',2),('a',2),('c',1),('c',4),('b',3)]
dicc = defaultdict(list) # Contiene una lista
for t in lista_tupla:
    # No es necesario consultar si el elemento que será la clave ya está en el diccionario
    dicc[t[0]] = t[1] # Es lo mismo que dic[t[0]].append(t[1])
print(dicc)

dicc2 = defaultdict(list) # Contiene una lista
for x,y in lista_tupla:
    dicc2[x] = y
print(dicc2)

palabras = ["plátano", "pera", "melón", "piña", "mango", "papaya", "melocotón", "sandia", "naranja"]