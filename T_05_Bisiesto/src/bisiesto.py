

def es_Bisiesto(anyo):
    #return anyo % 4 == 0  or (anyo % 100 != 0 or anyo % 400 == 0)
    return anyo % 4 == 0 or (anyo % 4 == 0 and anyo % 100 == 0)

