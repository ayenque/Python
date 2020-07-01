#range(comienzo, fin , pasos)

mi_rango  = range(1,5)
type(mi_rango)

for i in mi_rango:
    print(i)


mi_rango  = range(0,7,2)
mi_otro_rango  = range(0,8,2)

print(mi_rango == mi_otro_rango)

for i in mi_rango:
    print(i)

for i in mi_otro_rango:
    print(i)


print(id(mi_rango))
print(id(mi_otro_rango))
print(mi_rango is mi_otro_rango)


pares = []
for i in range(0,101,2):
    pares.append(i)

print(pares)

nones = []
for i in range(1,100,2):
    nones.append(i)

print(nones)


pares = list(range(0,101,2))
nones = list(range(1,100,2))
print(pares)
print(nones)
