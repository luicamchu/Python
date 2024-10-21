
f = open("x.cvs")
f.close()

with open("fichero.txt", mode="r", encoding="utf-8") as f1:
    contenido = f1.read()
    print(contenido)

with open("fichero.txt", mode="w", encoding="utf-8") as f2:
    f2.write("1\n")
    f2.write("2\n")
    f2.write("3\n")

with open("fichero.csv", mode="r", encoding="utf-8") as c1:
    numLineas = 0
    for linea in c1:
        print(linea)
        numLineas += 1
        if numLineas == 10:
            break
    
import csv# uso esta libreria para tratar un fichero con una estructura
with open("fichero.csv", mode="r", encoding="utf-8") as c2:
    lector = csv.reader(c2, delimiter=",")
    next(lector)
    for linea in lector:
        print(linea)
        break

Lista = [["1", "uno"],
         ["2", "dos"]]
with open("fichero.csv", mode="w", newline="") as c3:
    writer = csv.writer(c3, delimiter="|")
    writer.writerow(Lista)

try:
    res = 1
    for i in range(5, 0, -1):
        res *= 5/(i-1)
except Exception as e:
    print(e)
except ZeroDivisionError:
    print("Error: Division por 0")