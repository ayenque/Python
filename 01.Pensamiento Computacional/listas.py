mi_lista = [1,2,3]

print(mi_lista[0])
print(mi_lista[1:])


mi_lista.append(4)
print(mi_lista)

mi_lista[0] = 'a'

print(mi_lista)


mi_lista.pop() #elimina el ultimo elemento de la lista
mi_lista.pop()
print(mi_lista)

for elemento in mi_lista:
    print(elemento)

a = [1,2,3]
b = a   # Tener cuidado porque en realidad ambas estan apuntando a la misma memoria en realidad son lo mismo

print (id(a), id(b))


#Clonacion

a = [1,2,3]
b = a
c = list(a)   #clonar con list
d = a[::]    #clonar con slices
print(id(a),id(b),id(c),id(d))

mi_lista = list(range(100))
print(mi_lista)

doble = [i*2 for i in mi_lista]
print(doble)

pares = [i for i in mi_lista if i % 2 == 0 ]
print(pares)

pares = [i*2 for i in mi_lista if i % 2 == 0 and i > 50 ]
print(pares)