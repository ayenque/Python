import time
import math

def devolverRaizEnumeracion(objetivo):
    respuesta = 0
    tiempoInicial = time.time()
    iteraciones = 0

    while respuesta**2 < objetivo:
        #print(respuesta)
        respuesta += 1
        iteraciones += 1

    if (respuesta**2 != objetivo):
        respuesta = 'No se pudo calcular, raiz exacta' 
    
    tiempoTotal = time.time() - tiempoInicial
    
    return objetivo,respuesta,tiempoTotal,iteraciones
    


def devolverRaizAproximacion(objetivo):
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
        respuesta = 'No se pudo calcular, raiz exacta' 

    tiempoTotal = time.time() - tiempoInicial

    return objetivo,respuesta,tiempoTotal,iteraciones


def devolverRaizBusqueda(objetivo):
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0,objetivo)
    respuesta = (alto + bajo) / 2
    tiempoInicial = time.time()
    iteraciones = 0

    while abs(respuesta**2 - objetivo) >= epsilon:
        #print(f'bajo = {bajo} , alto = {alto} , respuesta = {respuesta}')
        if (respuesta**2 < objetivo):
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
        iteraciones += 1

    tiempoTotal = time.time() - tiempoInicial

    return objetivo,respuesta,tiempoTotal,iteraciones



def imprimirRespuesta(objetivo,respuesta,tiempo,iteraciones):
    print('\nResultados:  ')
    print('_' * 50)
    print(f'La raiz cuadrada de {objetivo} es {respuesta}.')
    print(f'El tiempo de ejecución de este script es de : {tiempo} segundos.')
    print(f'La cantidad de iteraciones fueron : {iteraciones}')



def saludo():
    print('Bienvenido vamos a calcular la raiz cuadrada √ de un número ... ')
    print('=' * 50)
    numero = int(input('Por favor ingrese un numero: '))
    print('Ingresar un metodo a utilizar:')
    print('\t|[1] "Enumeracion exhaustiva"    |')
    print('\t|[2] "Aproximacion de soluciones"|')
    print('\t|[3] "Busqueda binaria"          |')

    opcion = int(input('Elegir el numero de la opción: '))

    return numero, opcion


def seleccionarMetodo(objetivo, opcion):

    if (opcion == 1):
        print('\nEnumeracion Exhaustiva')
        o,r,t,i = devolverRaizEnumeracion(objetivo)
        imprimirRespuesta(o,r,t,i)
    elif (opcion == 2):
        print('\nAproximacion de Soluciones \nEspere...')
        o,r,t,i = devolverRaizAproximacion(objetivo)
        imprimirRespuesta(o,r,t,i)
    elif (opcion == 3):
        print('\nBusqueda Binaria')
        o,r,t,i = devolverRaizBusqueda(objetivo)
        imprimirRespuesta(o,r,t,i)
    else:
        print('\nSelección invalida, por favor elegir una opción de la lista')

    
if __name__ == "__main__":  
    objetivo, opcion = saludo()
    seleccionarMetodo(objetivo, opcion)