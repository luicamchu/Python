

from tratarFicheroCSV import *

numero = "05"
nombre = "Cadiz"

crearFicheroCSV2(numero, nombre)

datos='''Código,Provincia
01,Alava
02,Albacete'''

nombre="data\\provincias.csv"

crearFicheroCSV(nombre, datos)

leer(nombre)
