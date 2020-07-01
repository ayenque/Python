import math

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}

print(double_dict1)

dict1_keys = {k*2:v for (k,v) in dict1.items()}

print(dict1_keys)


# Initialize `fahrenheit` dictionary
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)




# Initialize the `fahrenheit` dictionary
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)




dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}

print(dict1_cond)

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}

print(dict1_doubleCond)




dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

print(dict1_tripleCond)




dic_nested = {'first':{'a':2}, 'second':{'b':4}}
dic_nested_f = {k_out: {k_in*2:float(v_in) for (k_in, v_in) in v_out.items()} for (k_out, v_out) in dic_nested.items()}
print(dic_nested_f)
print(type(dic_nested))


#{'first': {'aa': 2.0}, 'second': {'bb': 4.0}}