def func1 (un_arg, cualquier_func):  #func1(un_arg , una_func)
    def func2(un_arg):              # queda en memoria
        return un_arg * 2
    
    valor = func2(un_arg)   # llama a la linea 2 , retorna linea  3  y este se almacena en valor
    return cualquier_func(valor)  # llama a la linea 8 retorna linea 9, regresa a la linea 16

def cualquier_func(valor):  # queda en memoria
    return valor + 5

#____________________________________________________________________________

# Aquie se ejecuta primero, empieza por aquí : 
un_arg = 1
print(func1(un_arg,cualquier_func))  # llama a la linea 1 , envia por parametro un_arg que vale 1 y la funcion cualquier_func de la linea 8, continua en linea 1
                                     # Recibe el valor de linea 6 ( un_arg * 2 + 5 = 1*2 + 5 = 7) e imprime

