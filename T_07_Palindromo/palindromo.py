

def esPalindromo (palindromo)->bool:
    print(""+str(len(palindromo)))
    if (len(palindromo) <= 1):
        return True
    for i in range(0, len(palindromo)/2):
        if (palindromo[i] != palindromo[len(palindromo) - 1]):
            return False
    return False