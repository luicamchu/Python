#mas formatos para sacar por print
#format
nombre = "Luis"
print("Soy Luis")
print("Soy {:5s}".format(nombre))
print("Soy {:>5s}".format(nombre))

año = 2024
print("Feliz {:d}!".format(año))
print("Feliz {:10d}!".format(año))
print("Feliz {:<10d}!".format(año))
print("Feliz {:010d}!".format(año))

#{:n.df}
saldo = 234.45454
print("Mi saldo: {:10.2f} euros.".format(saldo))
print("Mi saldo: {:>2.2f} euros.".format(saldo))

#combinar valores y fromatos.

import math 
from math import sqrt
#depende de como hayas hecho el import condiciona a como llamas a la funcion.
import random
a = random.randint(1,10)
from random import randint
b = randint(1,10)

#tipos de agregados o secuencias

#inmutables
#cadena 
#tupla

#mutables
#conjunto(unicos, no ordenados), lista() , diccionario(tuplas(k,v))
#tuplas 

#set
#no odenados, no elementos repetidos y mutables
#conjunto.add(dato)/.remove(dato)/.discard(dato)

serVacio = set()
serVacio = {}#lo confunde con el diccionario

edades = {23, 14, 1, 134, 23, 14, 1}

#recorrer el conjunto

for e in edades:
    print(e)
    #recorre la lista que tiene almacenada, de datos no repetidos y no hay orden.





