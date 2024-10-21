calendarioEventos = list()
#eventos = list()

fecha_hora = []
descripcion = list()

import datetime

f1 = datetime.datetime.now()
d1 = "Cita medico."
f2 = datetime.datetime(2000, 1, 1)
d2 = "Clases."
f3 = datetime.datetime.now()
d3 = "Partido."

def añadirEvento(f, d ):
    fecha_hora.append(f)
    descripcion.append(d)

def borrarEvento(f):
    if f in fecha_hora:
        indiceFechaEvento = fecha_hora.index(f)
        fecha_hora.pop(indiceFechaEvento)
        descripcion.pop(indiceFechaEvento)
    

def listarEventos(l1, l2):
    print("Listado de Eventos:")
    for i in range(0, len(l2)):
        print("La fecha es: " + str(l1[i]) + " y la descripcion es: " + str(l2[i]))

añadirEvento(f1, d1)
añadirEvento(f2, d2)
añadirEvento(f3, d3)
listarEventos(fecha_hora, descripcion)

from datetime import datetime, date, timedelta

añadirEvento(datetime(2025, 1, 1, 17, 00, 00), "Dormir")
listarEventos(fecha_hora, descripcion)






