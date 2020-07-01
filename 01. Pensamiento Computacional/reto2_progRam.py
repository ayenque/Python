#Comparar las edades de dos usuarios y que indique el nombre de los mismos, junto con el resultado de las comparaciones.
print("----------------Bienvenido-------------------------")
nombre1 = input('Por favor ingrese el primer nombre: ')
nombre2 = input('Por favor ingresar el segundo nombre: ')
edad1 = int(input(f'Por favor ingresar la edad de {nombre1}: '))
edad2 = int(input(f'Por favor ingresar la edad de {nombre2}: '))
print("Gracias ....")

if (edad1 > 0 and edad2 > 0):
    if (edad1 > edad2):
        print(f'{nombre1} es mayor que {nombre2}')
    elif (edad1 < edad2):
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print('Ambos tienen la misma edad,',edad1, 'años.')
else:
    print('Por favor ingresar una edad correcta.')


