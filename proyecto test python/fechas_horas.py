from datetime import date

#fecha = date()
fecha_actual = date.today()
fecha_ayer = date(2024,9,22)
#print(fecha)
print(fecha_actual)
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

#horas
from datetime import time

#hora = time()
hora_pasada = time(17,30,12)
hora_ahora = time()

#datetime
from datetime import datetime

#fecha_hora = datetime()
fecha_hora_pasada = datetime(1996,3,15,23,30,00)
fecha_hora_ahora = datetime.now()

#formato
#striptime()
#dt_formateado = datetime().strptime()






#Ejemplos con fechas y horas
print("Ejemplos con fechas y horas: ")
from datetime import date,time,datetime,timedelta

#fecha y hora de hoy
print("Hoy es (fecha y hora): " + str(datetime.now()))

#fecha de hoy
print("La fecha de hoy es: " + str(date.today()))

#sumar un año a la fecha y hora actual
print("Fecha y hora actual + 1 año: " + str(datetime.now() + timedelta(days=365)))
print("Fecha actual + 1 año: " + str(date.today() + timedelta(days=365)))


#fijar la fecha a el 1 de enero del año actual
print("El primer día del año fue: " +str(date(2024,1,1)))

#el numero de dias que han pasado desde el inicio del año hasta hoy
print("Desde el 1 de enero 2024 han pasado " + str((date.today() - date(2024,1,1)).days) +" dias.")






