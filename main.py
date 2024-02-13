import math
from decimal import Decimal

list = ['Howard', 'Miller-McIntyre', 
        'Díez', 'Rogkavopoulos', 'Diop']
print(list)
# Tuple
tuple = (1, 2, 3, 4, 5)
print(tuple)
# Float
float = 1.5
print(float)
# Integer
integer = 5
print(integer)
# Decimal
decimal = Decimal('10.5')
print(decimal)
# Dictionary
dictionary = {1: 'Sivera', 2: 'Gorosabel', 3: 'Duarte'}
print(dictionary)

# Ejercicio 2 - Round your float up.
float_rounded = round(float)
print(round(float_rounded))

# Ejercicio 3 - Get the square root of your float.
float_square_root = math.sqrt(float)
print(float_square_root)

# Ejercicio 4 - Select the first element from your dictionary.
first_element_dict = dictionary[1]
print(first_element_dict)

# Ejercicio 5 - Select the second element from your tuple.
second_element_tpl = tuple[1]
print(second_element_tpl)

# Ejercicio 6 - Add an element to the end of your list.
list.append('Raieste')
print(list)

# Ejercicio 7 - Replace the first element in your list.
list[0] = 'Kotsar'
print(list)

# Ejercicio 8 - Sort your list alphabetically.
list.sort()
print(list)

# Ejercicio 9 - Use reassignment to add an element to your tuple.
tuple = tuple + (6,)
print(tuple)

