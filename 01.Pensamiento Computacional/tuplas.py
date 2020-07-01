
mi_tupla = ()

print(type(mi_tupla))

mi_tupla = (1, 'dos', True)

print(mi_tupla[0])

mi_tupla = (1,)

print(type(mi_tupla))

mi_otra_tupla = (2,3,4)

mi_tupla += mi_otra_tupla

print (mi_tupla)

x , y , z = mi_otra_tupla

print(x)
print(y)
print(z)

def coordenadas():
    return (5,4)

coordenada = coordenadas()

print(coordenada)

x , y = coordenada

print(x)
print(y)


mi_tupla = (1, 'dos', True)
mi_lista = list(mi_tupla)
print("Antes: ",mi_tupla)
mi_lista[2] = 'III' 
mi_tupla = tuple(mi_lista)
print("Despues: ",mi_tupla)

