#Ejercicio

from collections import namedtuple


Libro = namedtuple('Libro', 'titulo, año')
libros = [Libro("100 años de soledad", 1967), \
          Libro("1942", 1949), Libro("El quijote", 1605), \
            Libro("El principito", 1943)]

#1
sorted(libros, key=lambda x:x[1])
print("Lista ordenada por los años de los libros: "+ str(sorted(libros, key=lambda x:x.año)))

#2
min(libros, key=lambda x:x[1])
print("El libro mas antiguo es : " + str(min(libros, key=lambda x:x.año)))

#3
max(libros, key=lambda x:x[1])
print("El libro mas reciente es : " + str(max(libros, key=lambda y:y.año)))

#sort,sorted
libros.sort(key=lambda x: x.año)
print(libros)#la lista a mutado, se ha ordenado.
#print(str(libros.sort(key=lambda x: x.año))#devuelve nono porque es una funcion que no retorna nada. ordena)


#
#listaLetras = [l.letra for l in lista]
#
#listaMayores20 = [l.letra for l in lista if l.numero > 20]

conjuto = set()
#conjunto_letras  = {(l.numero, l.letra) for l in lista if l.numero > 20}



#filter
numeros = [0,10,2,3,14,35,56,474,4]

pares = list(filter(lambda x: x % 2 == 0, numeros))


n_producto_2 = list(map(lambda x: x*2))

#any()/all()

hay_par = any(x % 2 == 0 for x in numeros)

todos_positivos = all(x > 0 for x in numeros)



