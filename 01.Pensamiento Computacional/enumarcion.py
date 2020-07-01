import time
import math

objetivo = int(input('Escoge un entero: '))
respuesta = 0
tiempoInicial = time.time()


while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if (respuesta**2 == objetivo):
    print(f'La raiz cuadra de {objetivo} es {respuesta}.')
else:
    print(f'El objetivo no tiene una raiz cuadrada exacta, su raiz aproximada es : {math.sqrt(objetivo)}') 


print(f'El tiempo de ejecución de este script es de : {time.time()-tiempoInicial} segundos.')