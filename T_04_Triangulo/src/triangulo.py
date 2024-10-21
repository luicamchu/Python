from math import sqrt

def perimetro(a, b, c):
    return a+b+c

#ADDED
def es_triangulo(a,b,c) -> bool:
    return (a + b > c and a + c > b and b + c > a)

def area_h(a, b, c):
    #ADDED
    if((a <= 0 or b <= 0 or c <= 0) or not es_triangulo(a, b, c)):
        return None

    s = (perimetro(a, b, c) / 2)
    area = sqrt(s * (s-a) * (s-b) * (s-c))
    return area