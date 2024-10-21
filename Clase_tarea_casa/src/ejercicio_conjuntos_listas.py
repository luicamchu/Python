
set1 = set()
set2 = set()

set1.add('1')
set1.add('2')
set1.add('3')
set1.add('4')
set1.add('5')


set2.add('4')
set2.add('5')
set2.add('6')
set2.add('7')
set2.add('8')

setUnion = set1.union(set2)
setIntersection = set1.intersection(set2)
setDifference = set1.difference(set2)
setSD = set1.symmetric_difference(set2)

print(setUnion)
print(setIntersection)
print(setDifference)
print(setSD)

#listas
l = list()
l1 = []

#mutable, añadir-eliminar-modificar un dato,
l.append(1)
l.insert(1, 2)
l.remove(1)
l.index(2)
l.pop()
l1.append("a")
l1.append("b")
l1[-1]
l1[0]

miLista = [60,56, 79,23, 57,23]
for l in miLista:
    print(l + 1)

for pos in range(0, len(miLista)):
    print("Dato: " + str(miLista[pos]) + " de mi lista tiene la posicion: "
           + str(miLista.index(miLista[pos])))

#tuplas
#almacenar mas de un dato de un mismo contexto

tupla = ("122221212j", "ana l a", "F", 19, "Sevilla", "Sevilla")

persona1 = ("122221212j", "ana l a", "F", 19, "Sevilla", "Sevilla")
persona2 = ("122221212j", "jose l a", "F", 29, "Sevilla", "Sevilla")
persona3 = ("122221212j", "daniel l a", "F", 9, "Sevilla", "Sevilla")

persona1[1]
persona1[5]

persona2[-1]

persona3[1][3]

#namedtuple
#dotar de nombre a las columnas
from collections import namedtuple
#nt = namedtuple("nombre", "1,2,3")

#typename, field_names
Persona = namedtuple("persona", "dni, nombre, sexo, edad, localidad, provincia")
persona5 = Persona("122221212j", "lala l a", "F", 39, "Sevilla", "Sevilla")

persona5.nombre
persona5.dni

setPersonas = {Persona("122221212j", "lala l a", "F", 39, "Sevilla", "Sevilla"),Persona("122221212j", "lala l a", "F", 39, "Sevilla", "Sevilla")}

for p in setPersonas:
    print(p)

#for nombre,edad,sexo in setPersonas:
#    print(nombre, ":", edad)

for i in setPersonas:
    print(i.nombre, ":", i.edad)

#+ se puede usar con str, list, tupla, pero no con conjuntos.

#in T or F segun contenedor contenga el elemento. Con str, elementos de listas, tuplas

