import time

objetivo = int(input('Ingrese un numero :  '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0
tiempoInicial = time.time()
iteraciones = 0

while (abs(respuesta**2 - objetivo) >= epsilon and respuesta<=objetivo):
    #print(abs(respuesta**2- objetivo),respuesta)
    respuesta += paso
    iteraciones += 1

if (abs(respuesta**2 - objetivo) >= epsilon):
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

print(f'El tiempo de ejecución de este script es de : {time.time()-tiempoInicial} segundos.')
print(f'La cantidad de iteraciones fueron : {format(iteraciones)}')