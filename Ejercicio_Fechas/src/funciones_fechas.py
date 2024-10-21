
from datetime import date,datetime,time,timedelta
def restaFechas(fecha1, fecha2):
    f1 = datetime.strptime(fecha1, "%d/%m/%Y")
    f2 = datetime.strptime(fecha2, '%d/%m/%Y')
    if((f1 - f2).days < 0):
        return None
    return (f1 - f2).days


def sumaFechas(fecha, numDias):
    if(numDias < 0):
        return None
    f1 = datetime.strptime(fecha, "%d/%m/%Y")
    fecha_sumada = f1 + timedelta(days=numDias)
    return fecha_sumada
    
dias=restaFechas("23/09/2024", "15/03/2000")

print(str(dias))
print(sumaFechas("15/03/2000", dias))

dias_neg=-dias

print(restaFechas("15/03/2000", "23/09/2024"))
print(sumaFechas("15/03/2000", dias_neg))
