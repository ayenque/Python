my_dict = {'David' : 35 , 'Erika': 32, 'Jaime':50 , }  # llave para diccionario

print(my_dict['David'])
# print(my_dict['Erik'])
print(my_dict.get('Erik', 50))
print(my_dict.get('David', 50)) # 35
my_dict['Jaime'] = 20
print(my_dict)
my_dict['Pedro'] = 70
print(my_dict)

del my_dict['Jaime']

for llave in my_dict.keys():
    print(llave)

for valor in my_dict.values():
    print(valor)

for llave , valor in my_dict.items():
    print(llave,valor)

print('David' in my_dict)
print('Tom' in my_dict)

