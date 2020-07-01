

def genera_lambda(n):
  return lambda a : a * n


duplicar = genera_lambda(2)
tiplicar = genera_lambda(3)

print(duplicar(11))
print(tiplicar(11))




x = lambda a,n : a * n

print(x(2,11))
print(x(3,11))