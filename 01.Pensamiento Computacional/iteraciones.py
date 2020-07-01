'''
print(iter('cadena')) # cadena
print(iter(['a', 'b', 'c'])) # lista
print(iter(('a', 'b', 'c'))) # tupla
print(iter({'a', 'b', 'c'})) # conjunto
print(iter({'a': 1, 'b': 2, 'c': 3})) # diccionario


frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
        print(fruta)



frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

diccionario = {'a': 1, 'b': 2, 'c': 3}

for i,j in diccionario.items():
    print(i,j)

'''

regla = {'----Bienvenido -----': 18 ,'------Bienvenido, tenemos una promoción -----': 25}


numEdad = int(input('Por favor ingrese su edad: '))
flag = False
txtMensaje = ''

for mensaje, edad in regla.items():
    if numEdad >= edad:
        flag = True
        txtMensaje = mensaje

        
if flag:
    print(f'{txtMensaje}')
else:
    print('Acceso denegado')
