
from bisiesto import *

anyo:int = int(input("Introduce un año yyyy: "))

if (es_Bisiesto(anyo)):
    print(str(anyo) + " Es año bisiesto.")
else:
    print(str(anyo) + " No es año bisiesto.")