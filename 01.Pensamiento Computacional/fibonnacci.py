def fibonnacci(n):
    if (n == 1 or n == 0):
        return 1

    return fibonnacci(n-1) + fibonnacci(n-2)


numero = int(input('Ingrese la cantidad de numeros a generar : '))

for i in range(numero+1):
    print(f'Num {i} ==> {fibonnacci(i)}')
