from palindromo import *

palabra:str = str(input("Inttroduce una cadena de caracteres: "))
esPalindromo(palabra)
print(""+ str(palabra) + " es un palindromo" if esPalindromo(palabra) else " no es un palindromo")
