#factorial
def factorial (numero:int):
    fact:int = 1
    resultado:int = numero
    for i in range(1, numero+1):
        fact = fact * i
    while (numero != 1):
        resultado = resultado * (numero -1)
        numero = numero - 1
    print(resultado)
    return fact

#numero cambiado
def numero_c (num1:int, num2:int):
    cu = factorial(num1)
    cd = factorial(num2)
    cf = (cu / cd)
    return cf