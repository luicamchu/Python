
examen1 = [('alicia', 85), ("jose", 78), ('carlos', 92), ("david", 88)]
examen2 = [('alicia', 90), ("eva", 88), ('jose', 75), ("francisco", 84)]

#1
conjuto_tuplas = {x for x in examen1 + examen2 }
print(conjuto_tuplas)

#2
ambos_examenes = {x for x in set(examen1) & set(examen2) }
print(ambos_examenes)

ambos_examenes = {e[0] for e in set(examen1).intersection(f[0] for f in set(examen2))}


ambos_examenes = {e[0] for e in set(examen1).difference(f[0] for f in set(examen2))}


#puntuaciones

p_ambos = [(e[1],f[1]) for e in set(examen1) for f in set(examen2) if e[0] == f[0]]

media = [(p1 + p2)/2 for p1, p2 in p_ambos]

media_total = sum(media)