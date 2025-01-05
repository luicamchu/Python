from collections import Counter

palabras = ["kiwi", "pera", "melon", "mango", "pera", "kiwi", "piña", "kiwi", "piña"]

dict_frutas = Counter(palabras)

print(f"{dict_frutas.most_common(5)}")
for x in dict_frutas.most_common(5):
    print(f"\t{x}")

for p,c in dict_frutas.items():
    print(f"\t {p}: {c}")
print(f"{dict_frutas.most_common(5)[0]}")
print(f"{dict_frutas.most_common(5)[4]}")



#contador manualmente
lista_letras = ["a", "b", "c"]
dict_letras = dict()
for letra in lista_letras:
    if letra not in lista_letras:
        dict_letras[letra] = 0
    else:
        #dict_letras[letra] += 1
        pass

#lista de nametuple

#defaultdict
from collections import defaultdict
#defaultdict contiene una lista
lista_tuples = [("pepe",12),("jose", 11)]
dict_default = defaultdict(list)
for t in lista_tuples:
    pass


palabras2 = ["platano", "pera", "melon", "piña", "mango", "papaya" ,"melocoton", "sandia", "naranja"]

dict_primera_letra = dict()
print(dict_primera_letra)
for letra in palabras2:
    if letra[0] not in dict_primera_letra:
        dict_primera_letra[letra[0]] = 1
    else:
        dict_primera_letra[letra[0]] += 1
print(f"\t{dict_primera_letra}")


for l, c in dict_primera_letra.items():
    print(f"\t {l}:{c}")

dict_primera_letra2 = defaultdict(int)

for p in palabras2:
    dict_primera_letra2[p[0].lower()] += 1

