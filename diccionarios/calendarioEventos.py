
dict_eventos = dict()
def agregarEvento(fecha, descripcion)-> dict:
    dict_eventos[fecha] = descripcion
    return dict_eventos

def borrarDiccionario(fecha):
    if dict_eventos.get(fecha, False) != False:
        del(dict_eventos[fecha])

def listarEventos():
    for clave, valor in dict_eventos.items():
        print(f"Fecha evento: {clave}, Descripcion: {valor}")

def eventosProximos():
    pass
