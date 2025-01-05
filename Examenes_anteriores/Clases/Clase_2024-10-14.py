from collections import namedtuple

conjunto1 = {2, 4, 4, 7.2}
conjunto2 = {8.2, 4, 2, 'a', '2', 7.2}
conjunto3 = {8.2, 4, 2, 'a', '2', 7.2}

# or, and, diferencia, diferencia simetrica
print(conjunto1 | conjunto2)
print(conjunto2 | conjunto1)

print(conjunto1 & conjunto2)
print(conjunto2 & conjunto1)

print(conjunto1 - conjunto2)
print(conjunto2 - conjunto1)

print(conjunto1 ^ conjunto2)
print(conjunto2 ^ conjunto1)

# < a subconjunto de b, no igual. <= a subconjunto de b, o igual
print(conjunto1 < conjunto2)
print(conjunto2 < conjunto1)

print(conjunto2 < conjunto3)
print(conjunto3 < conjunto2)

print(conjunto2 <= conjunto3)
print(conjunto3 <= conjunto2)

# lambda
n = lambda n: 2 * n
nm = lambda m, n: n + m
print(n(4))
print(nm(4,1))

tupla = ((2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t'))
lista = [(2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t')]
conjunto = {(2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t')}

# Método: clear
conjunto.clear()
print(conjunto)
lista.clear()
print(lista)

lista = [(2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t')]
# sort, solo para list               
lista.sort()
print(lista)   
lista.sort(reverse=True)
print(lista)
lista.sort(key=lambda x:x[1])
print(lista)
lista.sort(key=lambda e: e[1], reverse=True)
print(lista)

tupla = ((2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t'))
lista = [(2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t')]
conjunto = {(2,'a'),(5,'z'),(4,'c'),(9,'b'),(4,'c'),(6,'w'),(1,'t')}
# sorted, devuelve una lista
print(sorted(tupla))
print(sorted(lista))
print(sorted(conjunto))
print(sorted(conjunto, reverse=True))

print(sorted(tupla, key=lambda e:e[1]))
print(sorted(lista, key=lambda e:e[1]))
print(sorted(conjunto, key=lambda e:e[1]))
print(sorted(conjunto, key=lambda e:e[1], reverse=True))

# max, min
print(max(tupla))
print(min(tupla))
print(max(lista))
print(min(lista))
print(max(conjunto))
print(min(conjunto))
print(max(conjunto, key=lambda e:e[1]))
print(min(conjunto, key=lambda e:e[1]))

tupla = (2,4,4,7.2)
lista = [2,4,4,7.2]
conjunto = {2,4,4,7.2}

# sum
print(sum(tupla))
print(sum(lista))
print(sum(conjunto))

# len
print(len(tupla))
print(len(lista))
print(len(conjunto))

Par = namedtuple('pareja', 'numero, letra')
tupla = (Par(2,'a'),Par(5,'z'),Par(4,'c'),Par(9,'b'),Par(4,'c'),Par(6,'w'),Par(1,'t'))
lista = [Par(2,'a'),Par(5,'z'),Par(4,'c'),Par(9,'b'),Par(4,'c'),Par(6,'w'),Par(1,'t')]
conjunto = {Par(2,'a'),Par(5,'z'),Par(4,'c'),Par(9,'b'),Par(6,'w'),Par(1,'t')}

# sorted, max, min
print(sorted(tupla, key=lambda e:e.letra))
print(max(lista, key=lambda e:e.letra))
print(min(conjunto, key=lambda e:e.letra))

Libro = namedtuple('Libro', 'titulo, año')
libros = [Libro('Cien años de soledad', 1967), Libro('1984', 1949), \
Libro('Don Quijote', 1605), Libro('El principito', 1943)]

# Ordenar la lista de libros por el año de publicación
libros_ordenados = sorted(libros, key=lambda e: e.año)
print(libros_ordenados)

# Encontrar el libro más antiguo
libro_mas_antiguo = min(libros, key=lambda e: e.año)
print(libro_mas_antiguo) 

# Encontrar el libro más reciente
libro_mas_reciente = max(libros, key=lambda e: e.año)
print(libro_mas_reciente)

Lista = [Par("z",21),Par("a",62),Par("J",7),Par("b",56),Par("c",90),Par("z",21), \
Par("a",1),Par("b",10),Par("b",2),Par("a",21)]

#Si queremos obtener una nueva lista con sólo las letras haríamos:
listaLetras = [l.letra for l in lista]
#Si queremos obtener una lista de tuplas con el número y la letra de aquellas cuyo número es mayor de 20 haríamos:
lista_mayores = [(l.numero,l.letra) for l in lista if l.numero > 20]
#Si quisiéramos obtener un conjunto con sólo las letras haríamos:
conj_letras = {l.letra for l in lista}
#Si quisiéramos obtener un conjunto de tuplas con el número y la letra de aquellas cuyo número es mayor de 20 haríamos :
conj_mayores = {(l.numero, l.letra) for l in lista if l.numero > 20}
import random
clientes = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
diccionario_descuentos = {cliente:random.randint(1,100) for cliente in clientes}
print(diccionario_descuentos)

examen1 = [('Alicia', 85), ('José', 78), ('Carlos', 92), ('David', 88)]
examen2 = [('Alicia', 90), ('Eva', 88), ('José', 75), ('Francisco', 84)]

# 1. Convertir las listas a conjuntos de tuplas
conjunto_examen1 = set(examen1)
conjunto_examen2 = set(examen2)
# 2. Encontrar estudiantes que han hecho ambos exámenes
estudiantes_ambos = {e1[0] for e1 in conjunto_examen1}.intersection(e2[0] for e2 in conjunto_examen2)
print("Estudiantes (punto 2):", estudiantes_ambos)
# 3. Encontrar estudiantes que han hecho solo el primer examen
solo_examen1 = {e1[0] for e1 in conjunto_examen1}.difference(e2[0] for e2 in conjunto_examen2)
print("Estudiantes (punto 3):", solo_examen1)
# 4. Encontrar estudiantes que han hecho solo el segundo examen
solo_examen2 = {e2[0] for e2 in conjunto_examen2}.difference(e1[0] for e1 in conjunto_examen1)
print("Estudiantes (punto 4):", solo_examen2)
# 5. Encontrar estudiantes que han hecho solo un examen
solo_examen = {e1[0] for e1 in conjunto_examen1}.symmetric_difference(e2[0] for e2 in conjunto_examen2)
print("Estudiantes (punto 5):", solo_examen)
# 6. Calcular la media de las puntuaciones de los estudiantes que han hecho ambos exámenes
puntuaciones_ambos = [(e1[1], e2[1]) for e1 in conjunto_examen1 for e2 in conjunto_examen2 if e1[0] == e2[0]]
media_puntuaciones = [(p1 + p2) / 2 for p1, p2 in puntuaciones_ambos]
media_total = sum(media_puntuaciones) / len(media_puntuaciones) if media_puntuaciones else 0
print("Media de puntuaciones:", media_total)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter
# Crear lista/conjunto/tupla filtrando solo los números pares
numeros_pares1 = list(filter(lambda x: x % 2 == 0, numeros))
numeros_pares2 = set(filter(lambda x: x % 2 == 0, numeros))
numeros_pares3 = tuple(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares1)
print(numeros_pares2)
print(numeros_pares3)

numeros = [1, 2, 3, 4, 5]

#map
# Crear lista/conjunto/tupla multiplicando cada número por 2
resultado1 = list(map(lambda x: x * 2, numeros))
resultado2 = set(map(lambda x: x * 2, numeros))
resultado3 = tuple(map(lambda x: x * 2, numeros))

print(resultado1)
print(resultado2)
print(resultado3)

#any() / all()
numeros = [1, 3, 5, 7, 8]

hay_par = any(x % 2 == 0 for x in numeros)
print(hay_par) # Salida: True (porque 8 es par)

todos_positivos = all(x > 0 for x in numeros)
print(todos_positivos) # Salida: True (todos son positivos)

palabras = ["satélite", "sol", "luna", "estrella", "marte", "júpiter"]
