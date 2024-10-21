import csv

listaProvincias = [["03", "Andalucia"],
           ["04", "Barcelona"]]

def crearFicheroCSV2 (nombre:str, texto:str) -> bool:
    
    res:bool = True
    fila = texto.strip()#.split("\n")
    with open("data/provincias2.csv", mode="w", newline="", encoding="utf-8") as p:
        arrayProvincia = [nombre,fila]
        listaProvincias.append(arrayProvincia)
        writer = csv.writer(p, delimiter="|")
        for lp in listaProvincias:
            writer.writerow(lp)
    return res
    
def crearFicheroCSV (nombre:str, texto:str) -> bool:
    res:bool = True
    fila = texto.strip().split("\n")
    try:
        with open(nombre, mode="w", newline="", encoding="utf-8") as provincias:
            writer = csv.writer(provincias, delimiter="|")
            for f in fila:
                writer.writerow(f.strip().split("\n"))
    except IOError as e:
        print("Error en los datos insertados")
        return res
    except Exception as e:
        print("Error")
        return res
    return res

def leer (nombreFichero):
    with open(nombreFichero, mode="r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido)
