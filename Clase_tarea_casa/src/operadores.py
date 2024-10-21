#|,&
#< <=
#lambda
#una forma de escribir funciones sencillas mediante una expresion
#lambda n: 2 * n

#metodos y funciones sobre tuplas/listas/conjuntos

#clear
from collections import namedtuple


tupla = ((2,'a'),(3,'b'),(4,'c'))
lista = [(2,'a'),(3,'b'),(7,'c'),(6,'a'),(4,'b'),(8,'c')]
conjunto = {(1,'0'),(2,'a'),(3,'e'),(7,'g'),\
            (6,'f'),(4,'b'),(8,'c')}

#tupla.clear()
lista.clear()
conjunto.clear()

#sort, te manipula la lista
#tupla.sort()
lista.sort()
#sort(reverse=True)

lista.sort(reverse=True)

#sorted lambda
#key=lambda e:e[i]
#tupla.sort(key=lambda x:x[1])
lista.sort(key=lambda x:x[1])
#conjunto.sort(key=lambda x:x[1])

sorted(tupla, key=lambda e:e[1])
sorted(lista, key=lambda e:e[1])
sorted(conjunto, key=lambda e:e[1])

#mas, min, 

max(tupla)
#max(lista, key=lambda l:l[0])
#max(conjunto)

min(tupla)
min(tupla)
min(tupla)

#sum()
#len()
numbers = [1, 2, 3, 4, 5]
print(sum(numbers, 10))
#Resultado 5

numbers = [1, 2, 3, 4, 5]
print(len(numbers))
#Resultado 15




Par = namedtuple('pareja', 'numero, letra')





