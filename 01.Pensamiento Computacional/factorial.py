import sys
sys.setrecursionlimit(1000) 
print(sys.getrecursionlimit())


def factorial(n):
    """

    Calcula el factorial de n.

    n = int >0
    return n!

    """
    if (n == 1):
        return 1

    return n * factorial(n-1)

n = int(input('Escribe un entero : '))

print(factorial(n))


