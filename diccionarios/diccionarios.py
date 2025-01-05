

dic = dict()#dic = {}
dic1 = {"IIIS":90, "IIIC":51, "IIIS":90, "IIIC":51,}
conjunto = {"pepe", "jose", "joaquin"}

#clave:valor

#los diccionarios no tienen claves repetidas

dict_p = {"Eva":{41,"Cadiz"}, "Manuel":{11,"Sevilla"},"Javier":{24,"Murcia"}}

#get()

dict_p.get("Eva")
#si no lo encuentra devuelve None, no aborta el programa

dict_p.get("Eva", False)
dict_p.get("jose", 0)
dict_p.get("jose", False)

#insertar/modificar datos de un diccionario
#con una asignacion
dict_new = {"Eva":41, "Manuel":11,"Javier":24}

dict_new["Eva"] = 20
dict_new.clear()

del(dict_new["Manuel"])
del(dict_new["Jose"])#error y aborta - > controlar

clave = "Jose"
if dict_new.get(clave, False) != False:
    #del(dict_new["Jose"])

if dict_new.has_key("Jose"):
    del(dict_new["Jose"])


#items()
dict_new.items() #convierte a una lista o a un conjunto

list(dict_new.items())
set(dict_new.items())

for clave, valor in dict_new.items():
    print("Key: " + clave + "Value: " + valor)

#keys()

dict_new.keys()

list(dict_new.keys())
set(dict_new.keys())


#values()

dict_new.values()

list(dict_new.values())
set(dict_new.values())


#Counter -> from collections import counter

from collections import Counter

dict_cont = Counter("abcdefbfjfjsofljffgslgk")
print(f"Salida {dict_cont}")#vendria ordenado

#iterable -> puedes hacer un for y recorrer sus campos

#otro ejemplo
lista = [12,342,4,2,24,24,24,121312,1233,123,123,123,22,1,344,3,2,12,2]
dict2 = Counter(lista)

dict2[6]
dict2[123]

#most_common
print(f"mas comun 3 {dict2.most_common(3)}")#lista 3 tuplas

print(f"mas comun 3 {dict2.most_common(1)}")


print(f"mas comun 3 {dict2.most_common(3)[1]}")

print(f"mas comun 3 {dict2.most_common(3)[0][0]}")







